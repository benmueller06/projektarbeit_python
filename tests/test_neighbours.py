import unittest
from source.neighbours import neighbours, vis, numbers, trap_values

class TestNeighbours(unittest.TestCase):
    """
    Test class for the neighbours function.
    """

    def setUp(self) -> None:
        """
        This method is run before each test to reset the global variables.
        """
        global vis, numbers, trap_values
        vis.clear()  # Clear the visited list
        n = 5
        numbers = [[0 for _ in range(n)] for _ in range(n)]  # Reset numbers grid
        trap_values = [[' ' for _ in range(n)] for _ in range(n)]  # Reset trap_values grid

    def test_single_zero_cell(self) -> None:
        """
        Test that a single zero cell is processed correctly.
        """
        numbers[2][2] = 0  # Set a single zero cell
        neighbours(2, 2)
        self.assertIn([2, 2], vis)  # Check that the cell is marked as visited
        self.assertEqual(trap_values[2][2], '0')  # Check that the cell is displayed as '0'

    def test_recursive_zero_cells(self) -> None:
        """
        Test that neighboring zero cells are processed recursively.
        """
        numbers[2][2] = 0
        numbers[2][3] = 0
        numbers[3][2] = 0
        neighbours(2, 2)
        self.assertIn([2, 2], vis)
        self.assertIn([2, 3], vis)
        self.assertIn([3, 2], vis)
        self.assertEqual(trap_values[2][2], '0')
        self.assertEqual(trap_values[2][3], '0')
        self.assertEqual(trap_values[3][2], '0')

    def test_non_zero_cell(self) -> None:
        """
        Test that a non-zero cell is processed correctly.
        """
        numbers[1][1] = 3  # Set a non-zero cell
        neighbours(1, 1)
        self.assertIn([1, 1], vis)  # Check that the cell is marked as visited
        self.assertEqual(trap_values[1][1], '3')  # Check that the cell is displayed as '3'

    def test_no_revisit(self) -> None:
        """
        Test that already visited cells are not revisited.
        """
        numbers[0][0] = 0
        vis.append([0, 0])  # Mark the cell as already visited
        neighbours(0, 0)
        self.assertEqual(len(vis), 1)  # Ensure no duplicate visits

if __name__ == '__main__':
    unittest.main()