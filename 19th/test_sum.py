import unittest


class Test3Sum(unittest.TestCase):

    def setUp(self):
        print('setup')

    def tearDown(self):
        print('setup')

    def test_input(self):
        threeSum([1213,321,23,21,12,12])



if __name__ == '__main__':
    unittest.main()
    