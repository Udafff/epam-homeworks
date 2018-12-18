import unittest
from raises import raises

class MyCustomException(Exception):
    """My custom exception message"""
    pass

class TestRaisesDec(unittest.TestCase):
    def setUp(self):
        self.test_string = {"My shiny string",}

    def tearDown(self):
        pass

    def test_raises(self):
        @raises(MyCustomException)
        def return_str():
            return self.test_string + 7

        with self.assertRaises(MyCustomException):
            return_str()

        @raises(MyCustomException)
        def return_str():
            return self.test_string

        try:
            return_str()

        except MyCustomException:
            self.fail(msg="Raises exception in clean code. Shoud replace exception only if it occured.")