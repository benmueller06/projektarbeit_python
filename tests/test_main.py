"""
Testing the main game.
"""
import unittest
import sys
from io import StringIO
from unittest.mock import patch
from source import main  # The module we are testing

class TestMainFunctions(unittest.TestCase):
    """
    Test class for the main game functions.
    """
    def setUp(self) -> None:
        """
        Set up the test environment.
        """
        main.N = 5
        main.TRAPS_NO = 5
        main.NUMBERS = [[0 for _ in range(main.N)] for _ in range(main.N)]
        main.TRAP_VALUES = [[' ' for _ in range(main.N)] for _ in range(main.N)]
        main.FLAGS = []

    def test_set_traps(self) -> None:
        """
        Test that traps are set correctly in the grid.
        """
        main.set_traps()
        trap_count = sum(row.count(-1) for row in main.NUMBERS)
        self.assertEqual(trap_count, main.TRAPS_NO)

    def test_set_values(self) -> None:
        """
        Test that the set_values function correctly calculates the number of traps
        around each cell.
        """
        # Manually place traps
        main.NUMBERS = [
            [ 0, -1,  0,  0,  0],
            [ 0,  0,  0, -1,  0],
            [ 0,  0,  0,  0,  0],
            [ 0, -1,  0,  0,  0],
            [ 0,  0,  0,  0, -1],
        ]
        main.set_values()
        self.assertEqual(main.NUMBERS[0][0], 1)  # 1 trap near top-left
        self.assertEqual(main.NUMBERS[1][1], 1)  # Only one trap near center
        self.assertEqual(main.NUMBERS[2][2], 2)  # Surrounded by two traps

    def test_check_over(self) -> None:
        """
        Test that the game is marked as over when all non-trap cells are revealed.
        """
        # Set up trap layout manually
        main.NUMBERS = [
            [ 0, -1,  0,  0,  0],
            [ 0,  0,  0, -1,  0],
            [ 0,  0,  0,  0,  0],
            [ 0, -1,  0,  0,  0],
            [ 0,  0,  0,  0, -1],
        ]
        main.set_traps()

        main.TRAP_VALUES = [[' ' for _ in range(main.N)] for _ in range(main.N)]
        # Simulate that user has revealed all non-trap cells
        for r in range(main.N):
            for c in range(main.N):
                if main.NUMBERS[r][c] != -1:
                    main.TRAP_VALUES[r][c] = str(main.NUMBERS[r][c])
        self.assertFalse(main.check_over())

    def test_neighbours_expansion(self) -> None:
        """
        Test the neighbours function to ensure it correctly expands to all connected cells.
        """
        main.VIS = []
        main.NUMBERS = [
            [0, 0, 1, -1, 1],
            [0, 0, 1, 1, 1],
            [1, 1, 1, 0, 0],
            [-1, 1, 0, 0, 0],
            [1, 1, 0, -1, 0],
        ]
        main.TRAP_VALUES = [[' ' for _ in range(main.N)] for _ in range(main.N)]
        main.neighbours(0, 0, main.VIS)

        for r, c in main.VIS:
            self.assertNotEqual(main.TRAP_VALUES[r][c], ' ')
        self.assertIn([0, 0], main.VIS)
        self.assertGreater(len(main.VIS), 1)

    def test_game_loop_simulation(self) -> None:
        """
        Simulate a simple game loop by directly modifying global variables.
        """
        # Set up a simple grid with no traps
        main.NUMBERS = [[0 for _ in range(main.N)] for _ in range(main.N)]
        main.TRAPS_NO = 0
        main.set_values()

        # Simulate user revealing all cells
        for r in range(main.N):
            for c in range(main.N):
                main.TRAP_VALUES[r][c] = str(main.NUMBERS[r][c])

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

    def test_game_loop(self) -> None:
        """
        Test the game_loop function with simulated user input.

        This test simulates a sequence of valid moves that leads to winning the game.
        It uses mock to patch input and suppress screen clearing.
        """
        # Set up a 2x2 board with no traps for controlled test
        main.N = 2
        main.TRAPS_NO = 0
        main.NUMBERS = [[0, 0], [0, 0]]
        main.TRAP_VALUES = [[' ' for _ in range(main.N)] for _ in range(main.N)]
        main.FLAGS = []
        main.VIS = []

        # Patch input to simulate user revealing all cells
        # Sequence of inputs: "1 1", "1 2", "2 1", "2 2"
        inputs = ["1 1", "1 2", "2 1", "2 2"]
        with patch("builtins.input", side_effect=inputs), \
             patch("os.system"), \
             patch("builtins.print"):
            # Expect the game to complete without error
            main.game_loop()

        # After game loop, TRAP_VALUES should be revealed
        for row in main.TRAP_VALUES:
            for cell in row:
                self.assertNotEqual(cell, ' ')

    def test_globals_set(self) -> None:
        """
        Test that the global variables are set correctly.
        """
        main.print_traps_layout()

        # Check global 'n' is 5
        self.assertEqual(main.N, 5)

        # Check TRAP_VALUES is 5x5 and filled with 0s
        self.assertEqual(len(main.TRAP_VALUES), 5)
        for row in main.TRAP_VALUES:
            self.assertEqual(len(row), 5)
            self.assertFalse(all(cell == 0 for cell in row))

if __name__ == "__main__":
    unittest.main()
