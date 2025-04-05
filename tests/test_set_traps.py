"""
Testfile to test the set_traps module.
"""
import unittest
# Import the function to test
from source import set_traps

class TestSetTraps(unittest.TestCase):
    """
    Test class for the set_traps function.
    """
    def setUp(self) -> None:
        """
        This method is run before each individual test.
        It resets the game grid to its initial state (all zeros) 
        to make sure each test is independent.
        """
        set_traps.numbers = [[0 for _ in range(set_traps.n)] for _ in range(set_traps.n)]

    def test_trap_count(self) -> None:
        """
        Test that the correct number of traps are placed on the grid.
        A trap is represented by -1, so we count how many -1s exist
        and compare that to the expected number of traps.
        """
        set_traps.set_traps()
        trap_count = sum(row.count(-1) for row in set_traps.numbers)
        self.assertEqual(trap_count, set_traps.traps_no, "Incorrect number of traps set")

    def test_no_duplicate_traps(self) -> None:
        """
        Ensure that traps are not placed in the same cell more than once.
        This test collects all trap positions and checks that they are unique.
        """
        set_traps.set_traps()
        positions = [(r, c) for r in range(set_traps.n)# In two lines because line was too long
        for c in range(set_traps.n) if set_traps.numbers[r][c] == -1]
        self.assertEqual(len(positions), len(set(positions)), "Duplicate traps found")

    def test_only_valid_values(self) -> None:
        """
        Check that the grid contains only valid values (0 or -1).
        There should be no unexpected numbers after placing traps.
        """
        set_traps.set_traps()
        for row in set_traps.numbers:
            for val in row:
                self.assertIn(val, [0, -1], "Invalid value in grid")

# Run the tests when this script is executed
if __name__ == '__main__':
    unittest.main()
