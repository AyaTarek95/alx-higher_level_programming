#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unittest of max_integer([..])"""
    def test_no_arg(self):
        """Unittest of max_integer([..])"""
        self.assertEqual(max_integer(), None)
    
    def test_unordered_larger(self):
        """Unittest of max_integer([..])"""
        self.assertEqual(max_integer([23, 58, 91, 24, 1070, 89, 98,
                                     108, 256, 512]), 1070)

    def test_empty_list(self):
        """Unittest of max_integer([..])"""
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([75]), 75)

    def test_identical(self):
        """Unittest of max_integer([..])"""
        self.assertEqual(max_integer([6, 6, 6, 6]), 6)

    def test_max_start(self):
        """Unittest of max_integer([..])"""
        self.assertEqual(max_integer([10, 4, 3, 2]), 10)

    def test_ordered(self):
        """Unittest of max_integer([..])"""
        self.assertEqual(max_integer([1, 2, 3, 8]), 8)

    def test_ordered_larger(self):
        """Unittest of max_integer([..])"""
        self.assertEqual(max_integer([2, 4, 6, 8, 10, 12, 14, 16, 18, 50]), 50)

    def test_unordered(self):
        """Unittest of max_integer([..])"""
        self.assertEqual(max_integer([1, 3, 7, 2]),7)

    def test_positives_and_negatives(self):
        """Unittest of max_integer([..])"""
        self.assertEqual(
            max_integer([-23, 58, 91, 24, -1024, 89, 98, 205, -256, -512]),
            205)

    def test_negatives(self):
        """Unittest of max_integer([..])"""
        self.assertEqual(
            max_integer(
                [-6105619, -854849, -6711290, -4817844,
                    -1907189, -8110534, -6601769, -5837524, -4726702,
                    -8433749, -7251403, -5117635, -2979207, -1335257,
                    -6867266, -9073637, -6224732, -1080801, -1080228,
                    -6801278, -8351954, -1736432, -746131, -4376995,
                    -967891, -4663691, -71562, -7153670, -8038202,
                    -2839083, -2586661, -9941097]), -71562)

    def test_ints_and_floats(self):
        """Unittest of max_integer([..])"""
        self.assertEqual(
            max_integer(
                [10, 99.8, -100, -0.1, 1000, 9999, -100000, 9998.9]), 9999)
    
    def test_string(self):
        """Unittest of max_integer([..])"""
        self.assertEqual(max_integer("Albert"), "t")
     
    def test_numeric_string(self):
        """Unittest of max_integer([..])"""
        self.assertEqual(max_integer("095547321"), "9")

    def test_mixed_list_int_str(self):
        """Unittest of max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([80, "cool"])
    
    def test_str_list(self):
        """Unittest of max_integer([..])"""
        self.assertEqual(
            max_integer([["abc"], ["foo"], ["boo"], ["ric"], ["sic"]]),
            ["sic"])

    def test_inf(self):
        """Unittest of max_integer([..])"""
        self.assertEqual(max_integer([90, float('inf'), float('-inf')]),
                         float('inf'))

    def test_nan(self):
        """Unittest of max_integer([..])"""
        self.assertEqual(max_integer([98, float('nan'), 101]), 101)

    def test_mixed_list(self):
        """Unittest of max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([[], [5], [2], [2, 8], 97, "cool"])

if __name__ == "__main__":
    unittest.main()
