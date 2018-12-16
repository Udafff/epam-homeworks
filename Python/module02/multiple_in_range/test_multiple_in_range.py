from multiple_in_range import multiple_in_range
import unittest


class TestBetween(unittest.TestCase):

    def test_multiple_in_range(self):
        self.assertEqual(multiple_in_range(1, 77), [7, 14, 21, 28, 42, 49, 56, 63, 77])
        self.assertEqual(multiple_in_range(-77, 77),
                         [-77, -63, -56, -49, -42, -28, -21, -14, -7, 7, 14, 21, 28, 42, 49, 56, 63, 77])
        self.assertEqual(multiple_in_range(-77, -7), [-77, -63, -56, -49, -42, -28, -21, -14, -7])
        with self.assertRaises(TypeError, msg="multiple_in_range(0, 55.55)"):
            multiple_in_range(0, 55.55)
        with self.assertRaises(TypeError, msg='multiple_in_range(0, "")'):
            multiple_in_range(0, "")


if __name__ == "__main__":
    unittest.main()
