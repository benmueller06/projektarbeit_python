"""
Testfile to test the set_values module.
"""
import unittest
from source import set_values  # The module we are testing

class TestSetValues(unittest.TestCase):
    """
    Test class for the set_values function.
    """
    def setUp(self) -> None:
        """
        Reset the game grid to a known state before each test.
        We'll manually define a 5x5 grid with specific trap locations.
        """
        set_values.numbers = [[0 for _ in range(set_values.n)] for _ in range(set_values.n)]
        # Manually placing traps for consistent results
        # Traps placed at positions (1,1), (2,2), (3,3)
        trap_positions = [(1, 1), (2, 2), (3, 3)]
        for r, c in trap_positions:
            set_values.numbers[r][c] = -1

    def test_trap_cells_unchanged(self)-> None:
        """
        Ensure that trap positions remain -1 after calling set_values.
        """
        set_values.set_values()
        self.assertEqual(set_values.numbers[1][1], -1)
        self.assertEqual(set_values.numbers[2][2], -1)
        self.assertEqual(set_values.numbers[3][3], -1)

    def test_adjacent_values_correct(self)-> None:
        """
        Check that the values of cells adjacent to traps are correctly set.
        Each cell should contain the count of traps in its 8-neighbor area.
        """
        set_values.set_values()
        # Cell (1,2) is adjacent to traps at (1,1) and (2,2) -> value should be 2
        self.assertEqual(set_values.numbers[1][2], 2)
        # Cell (2,1) is adjacent to (1,1) and (2,2) -> value should be 2
        self.assertEqual(set_values.numbers[2][1], 2)
        # Cell (2,3) is adjacent to trap at (3,3) and (2,2) -> value should be 2
        self.assertEqual(set_values.numbers[2][3], 2)

    def test_only_valid_values(self)-> None:
        """
        Ensure all non-trap cells contain non-negative integers (counts),
        and traps remain -1.
        """
        set_values.set_values()
        for row in set_values.numbers:
            for val in row:
                self.assertTrue(val == -1 or val >= 0, "Invalid value in grid")

# Run the test when the file is executed
if __name__ == '__main__':
    unittest.main()
