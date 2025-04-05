"""
Unit tests for the neighbours function in the source module.
"""
import unittest
from source import neighbours  # The module we are testing

class TestNeighboursFunction(unittest.TestCase):
    """
    Test class for the neighbours function.
    """
    def setUp(self) -> None:
        # Reset global state before each test
        neighbours.n = 5
        neighbours.vis = []
        neighbours.trap_values = [[' ' for _ in range(neighbours.n)] for _ in range(neighbours.n)]
        neighbours.numbers = [[0 for _ in range(neighbours.n)] for _ in range(neighbours.n)]

    def test_single_zero_center(self) -> None:
        """
        Test a 5x5 grid with a single zero in the center.
        """
        # Only the center is 0, surrounded by non-zero cells
        neighbours.numbers = [
            [1, 1, 1, 1, 1],
            [1, 2, 2, 2, 1],
            [1, 2, 0, 2, 1],
            [1, 2, 2, 2, 1],
            [1, 1, 1, 1, 1],
        ]
        neighbours.neighbours(2, 2)

        # Check if only the center was visited
        self.assertIn([2, 2], neighbours.vis)
        self.assertEqual(neighbours.trap_values[2][2], "0")
        self.assertEqual(len(neighbours.vis), 9)

    def test_recursive_zeros(self) -> None:
        """
        Test a 5x5 grid with a 3x3 block of zeros in the center.
        """
        # A 3x3 zero block in the center
        neighbours.numbers = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]
        neighbours.neighbours(2, 2)

        # Expect all 9 zeros visited
        expected_visited = [
            [1, 1], [1, 2], [1, 3],
            [2, 1], [2, 2], [2, 3],
            [3, 1], [3, 2], [3, 3],
        ]
        for cell in expected_visited:
            self.assertIn(cell, neighbours.vis)
            self.assertEqual(neighbours.trap_values[cell[0]][cell[1]], '0')
        self.assertEqual(len(neighbours.vis), 25)

    def test_edge_case_top_left_corner(self) -> None:
        """
        Test a 5x5 grid with a zero in the top-left corner.
        """
        neighbours.numbers = [
            [0, 0, 1, 1, 1],
            [0, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ]
        neighbours.neighbours(0, 0)
        expected_visited = [[0,0],[0,1],[1,0]]
        for cell in expected_visited:
            self.assertIn(cell, neighbours.vis)

    def test_no_recursion_non_zero(self) -> None:
        """
        Test a 5x5 grid with a non-zero cell in the center.
        """
        neighbours.numbers = [
            [1, 1, 1, 1, 1],
            [1, 2, 2, 2, 1],
            [1, 2, 5, 2, 1],
            [1, 2, 2, 2, 1],
            [1, 1, 1, 1, 1],
        ]
        neighbours.neighbours(2, 2)
        self.assertEqual(neighbours.trap_values[2][2], '5')
        self.assertIn([2, 2], neighbours.vis)
        self.assertEqual(len(neighbours.vis), 1)

if __name__ == "__main__":
    unittest.main()
