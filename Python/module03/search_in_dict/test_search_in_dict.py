import unittest

from search_in_dict import search_in_dict


class TestBetween(unittest.TestCase):

    def test_search(self):
        # haystack = {str(x): x * 2 for x in reversed(range(1000000))}
        # self.assertEqual(search_in_dict(["1", "2", "1000", "testStr"], haystack), {"1", "2", "1000"})
        # self.assertEqual(search_in_dict({"1", "2", "1000", "testStr"}, haystack), {"1", "2", "1000"})

        haystack = {str(x): x * 2 for x in reversed(range(100))}
        # self.assertEqual(search_in_dict(["1", "2", "10", "testStr"], haystack), {"1", "2", "10"})
        self.assertEqual(search_in_dict({"1", "2", "10", "testStr"}, haystack), {"1", "2", "10"})

        with self.assertRaises(TypeError):
            search_in_dict({"1", "2", "1000", {}}, haystack)


if __name__ == "__main__":
    unittest.main()
