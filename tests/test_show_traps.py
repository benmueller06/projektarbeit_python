"""Unit tests for the show_traps function in the source module.
"""
import unittest
from source import show_traps  # The module we are testing


class TestShowTraps(unittest.TestCase):
    """
    Test class for the show_traps function.
    """
    def setUp(self) -> None:
        """
        Set up the test environment.
        """
        show_traps.n = 3
        show_traps.trap_values = [[' ' for _ in range(show_traps.n)] for _ in range(show_traps.n)]
        show_traps.numbers = [
            [ 0, -1,  0],
            [-1,  0,  0],
            [ 0,  0, -1]
        ]

    def test_show_traps_marks_only_traps(self) -> None:
        """
        Test that show_traps marks only the traps with 'M'.
        """
        show_traps.show_traps()

        expected = [
            [' ', 'M', ' '],
            ['M', ' ', ' '],
            [' ', ' ', 'M']
        ]
        self.assertEqual(show_traps.trap_values, expected)

    def test_show_traps_does_not_modify_safe_cells(self) -> None:
        """
        Test that show_traps does not modify non-trap cells.
        """
        # Before calling show_traps, make sure non-trap cells have distinct values
        show_traps.trap_values = [['x' for _ in range(show_traps.n)] for _ in range(show_traps.n)]
        show_traps.trap_values[0][1] = ' '
        show_traps.trap_values[1][0] = ' '
        show_traps.trap_values[2][2] = ' '
        show_traps.show_traps()

        self.assertEqual(show_traps.trap_values[0][1], 'M')
        self.assertEqual(show_traps.trap_values[1][0], 'M')
        self.assertEqual(show_traps.trap_values[2][2], 'M')
        self.assertEqual(show_traps.trap_values[0][0], 'x')  # untouched
        self.assertEqual(show_traps.trap_values[1][1], 'x')
        self.assertEqual(show_traps.trap_values[2][1], 'x')


if __name__ == '__main__':
    unittest.main()
