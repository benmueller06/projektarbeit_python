"""
Testfile to test the layout module.
"""
import unittest
from io import StringIO
import sys

# Import the function to test
from source import layout

class TestPrintTrapsLayout(unittest.TestCase):
    """
    Test class for the print_traps_layout function.
    """
    def test_print_traps_layout_output(self) -> None:
        """
        Test the output of the print_traps_layout function.
        """
        # Redirect stdout to capture print statements
        captured_output = StringIO()
        sys.stdout = captured_output

        layout.print_traps_layout()

        # Reset redirect.
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()

        # Check that the title and dimensions are present
        self.assertIn("SPACESTATION", output)
        self.assertIn("1     2     3     4     5", output)
        self.assertIn("|  0  |  0  |  0  |  0  |  0  |", output)

    def test_globals_set(self) -> None:
        """
        Test that the global variables are set correctly.
        """
        layout.print_traps_layout()

        # Check global 'n' is 5
        self.assertEqual(layout.n, 5)

        # Check trap_values is 5x5 and filled with 0s
        self.assertEqual(len(layout.trap_values), 5)
        for row in layout.trap_values:
            self.assertEqual(len(row), 5)
            self.assertTrue(all(cell == 0 for cell in row))

if __name__ == '__main__':
    unittest.main()
