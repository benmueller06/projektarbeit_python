import unittest
import layout
global n
global mine_values
 
class TestPrintMinesLayout(unittest.TestCase):
     def test_layout(self):
       result = layout.print_mines_layout()

       self.assertEqual(result, layout.print_mines_layout())

if __name__ == '__main__':
    unittest.main()