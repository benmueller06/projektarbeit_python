"""Unit tests for the check_over function in the source module.
"""
import unittest
from source import check_over


class TestCheckOver(unittest.TestCase):
    """
    Test class for the check_over function.
    """
    def setUp(self) -> None:
        check_over.n = 5
        check_over.traps_no = 5
        check_over.trap_values = [[0 for _ in range(check_over.n)] for _ in range(check_over.n)]

    def test_not_over_initial_state(self) -> None:
        """
        Test that the game is not over when no traps are revealed.
        """
        self.assertFalse(check_over.check_over())

    def test_game_completed(self) -> None:
        """
        Test that the game is completed when all non-trap cells are revealed.
        """
        # Simulate all non-trap cells revealed (20 revealed, 5 hidden)
        count = 0
        for r in range(check_over.n):
            for c in range(check_over.n):
                if count < check_over.n * check_over.n - check_over.traps_no:
                    check_over.trap_values[r][c] = 1
                    count += 1
                else:
                    check_over.trap_values[r][c] = 0

        self.assertFalse(check_over.check_over())

    def test_game_not_completed_due_to_flags(self) -> None:
        """ 
        Test that the game is not completed when there are flagged cells.
        """
        # Same as above but with one cell flagged instead of revealed
        count = 0
        for r in range(check_over.n):
            for c in range(check_over.n):
                if count < check_over.n * check_over.n - check_over.traps_no - 1:
                    check_over.trap_values[r][c] = 1
                    count += 1
                elif count == check_over.n * check_over.n - check_over.traps_no - 1:
                    check_over.trap_values[r][c] = -1  # Use -1 to represent flagged cells
                    count += 1
                else:
                    check_over.trap_values[r][c] = 0

        self.assertFalse(check_over.check_over())


if __name__ == "__main__":
    unittest.main()
