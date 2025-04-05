import unittest
import sys
from io import StringIO
from source import main  # The module we are testing

class TestMainFunctions(unittest.TestCase):

    def setUp(self) -> None:
        main.n = 5
        main.traps_no = 5
        main.numbers = [[0 for _ in range(main.n)] for _ in range(main.n)]
        main.trap_values = [[' ' for _ in range(main.n)] for _ in range(main.n)]
        main.flags = []

    def test_set_traps(self) -> None:
        main.set_traps()
        trap_count = sum(row.count(-1) for row in main.numbers)
        self.assertEqual(trap_count, main.traps_no)

    def test_set_values(self) -> None:
        # Manually place traps
        main.numbers = [
            [ 0, -1,  0,  0,  0],
            [ 0,  0,  0, -1,  0],
            [ 0,  0,  0,  0,  0],
            [ 0, -1,  0,  0,  0],
            [ 0,  0,  0,  0, -1],
        ]
        main.set_values()
        self.assertEqual(main.numbers[0][0], 1)  # 1 trap near top-left
        self.assertEqual(main.numbers[1][1], 1)  # Only one trap near center
        self.assertEqual(main.numbers[2][2], 2)  # Surrounded by two traps

    def test_check_over(self) -> None:
        # Set up trap layout manually
        main.numbers = [
            [ 0, -1,  0,  0,  0],
            [ 0,  0,  0, -1,  0],
            [ 0,  0,  0,  0,  0],
            [ 0, -1,  0,  0,  0],
            [ 0,  0,  0,  0, -1],
        ]
        main.set_traps()

        main.trap_values = [[' ' for _ in range(main.n)] for _ in range(main.n)]
        # Simulate that user has revealed all non-trap cells
        for r in range(main.n):
            for c in range(main.n):
                if main.numbers[r][c] != -1:
                    main.trap_values[r][c] = str(main.numbers[r][c])
        self.assertFalse(main.check_over())

    def test_neighbours_expansion(self) -> None:
        main.vis = []
        main.numbers = [
            [0, 0, 1, -1, 1],
            [0, 0, 1, 1, 1],
            [1, 1, 1, 0, 0],
            [-1, 1, 0, 0, 0],
            [1, 1, 0, -1, 0],
        ]
        main.trap_values = [[' ' for _ in range(main.n)] for _ in range(main.n)]
        main.neighbours(0, 0)

        for r, c in main.vis:
            self.assertNotEqual(main.trap_values[r][c], ' ')
        self.assertIn([0, 0], main.vis)
        self.assertGreater(len(main.vis), 1)

    def test_game_loop_simulation(self) -> None:
        """
        Simulate a simple game loop by directly modifying global variables.
        """
        # Set up a simple grid with no traps
        main.numbers = [[0 for _ in range(main.n)] for _ in range(main.n)]
        main.traps_no = 0
        main.set_values()

        # Simulate user revealing all cells
        for r in range(main.n):
            for c in range(main.n):
                main.trap_values[r][c] = str(main.numbers[r][c])

        # Check if the game is marked as over
        self.assertTrue(main.check_over())

    def test_print_traps_layout_output(self) -> None:
        """
        Test the output of the print_traps_layout function.
        """
        # Redirect stdout to capture print statements
        captured_output = StringIO()
        sys.stdout = captured_output

        main.print_traps_layout()

        # Reset redirect.
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()

        # Check that the title and dimensions are present
        self.assertIn("SPACESTATION", output)
        self.assertIn("1     2     3     4     5", output)
        self.assertIn("|     |     |     |     |     |", output)

    def test_globals_set(self) -> None:
        """
        Test that the global variables are set correctly.
        """
        main.print_traps_layout()

        # Check global 'n' is 5
        self.assertEqual(main.n, 5)

        # Check trap_values is 5x5 and filled with 0s
        self.assertEqual(len(main.trap_values), 5)
        for row in main.trap_values:
            self.assertEqual(len(row), 5)
            self.assertFalse(all(cell == 0 for cell in row))

if __name__ == "__main__":
    unittest.main()
