import unittest
from caesarCipher import CaesarCipherBetter

class TestCaesarCipher(unittest.TestCase):

    def setUp(self):
        self.input = '1:2231112Sadss21!##$AA:"DS'

    def tearDown(self):
        pass

    def test_colons(self):
        with self.assertRaises(ValueError):
            CaesarCipherBetter(self.input)

    # def test_noShift(self):
    #     with self.assertRaises(ValueError):
    #         s


    # def test_noinput(self):
    #     self.assertTrue()



if __name__ == '__main__':
    unittest.main()