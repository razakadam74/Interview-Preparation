import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2.0)
        self.assertEqual(calc.divide(10.5, 2),5.25)
        self.assertRaises(ValueError, calc.divide, 10, 0)

        with self.assertRaises(ValueError):
            calc.divide(10,0)
            

        


if __name__ == '__main__':
    unittest.main()
