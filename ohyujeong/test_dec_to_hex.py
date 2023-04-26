import unittest
from dec_to_hex import dec_to_hex

class TestDecimalToHexadecimal(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(dec_to_hex(255), 'FF')
        self.assertEqual(dec_to_hex(4096), '1000')
        self.assertEqual(dec_to_hex(65535), 'FFFF')

    def test_zero(self):
        self.assertEqual(dec_to_hex(0), '0')

    def test_negative_number(self):
        self.assertEqual(dec_to_hex(-1), 'FFFFFFFFFFFFFFFF')
        self.assertEqual(dec_to_hex(-255), 'FFFFFFFFFFFFFF01')

if __name__ == '__main__':
    unittest.main()
