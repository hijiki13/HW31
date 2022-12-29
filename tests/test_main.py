import unittest
from main import Int_nums

nums_ok = [1, 9, 13, 15, 88, 44, 123, 9, 3, 54, 62, 37]
nums_big = [1234, 5678, 9101, 1121, 3141, 5161, 7181, 9200]
nums_empty = []
nums_type = [15, True, 'str', 5, None, 2.2]
nums_same = [13, 13, 13, 13, 13, 13]
nums_not = '1, 2, 3, 5, 8, 13, 21, 34, 55, 89'

class MainTest(unittest.TestCase):
    is_ok = Int_nums(nums_ok)
    is_big = Int_nums(nums_big)
    is_same = Int_nums(nums_same)
    
    def test_validate(self):
        is_empty = Int_nums(nums_empty)
        is_not_type = Int_nums(nums_type)
        is_not = Int_nums(nums_not)

        self.assertFalse(is_empty.validate())
        self.assertFalse(is_not_type.validate())
        self.assertFalse(is_not.validate())

        self.assertTrue(self.is_ok.validate())
        self.assertTrue(self.is_big.validate())

    def test_sum(self):
        self.assertEqual(self.is_ok.sum(), sum(nums_ok))
        self.assertEqual(self.is_big.sum(), sum(nums_big))
        self.assertEqual(self.is_same.sum(), sum(nums_same))

    def test_mean(self):
        self.assertEqual(self.is_ok.mean(), sum(nums_ok)/len(nums_ok))
        self.assertEqual(self.is_big.mean(), sum(nums_big)/len(nums_big))
        self.assertEqual(self.is_same.mean(), nums_same[0])
        

    def test_max(self):
        self.assertEqual(self.is_ok.max_num(), max(nums_ok))
        self.assertEqual(self.is_big.max_num(), max(nums_big))
        self.assertEqual(self.is_same.max_num(), nums_same[0])
    
    def test_min(self):
        self.assertEqual(self.is_ok.min_num(), min(nums_ok))
        self.assertEqual(self.is_big.min_num(), min(nums_big))
        self.assertEqual(self.is_same.min_num(), nums_same[0])