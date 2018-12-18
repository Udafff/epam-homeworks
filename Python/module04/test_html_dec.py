import unittest
from html_dec import italic, bold, underline

class TestHtmlDec(unittest.TestCase):
    def setUp(self):
        self.test_string = "My shiny string"

    def tearDown(self):
        pass

    def test_italic(self):
        @italic
        def return_str():
            return self.test_string

        self.assertEqual(return_str(), f'<i>{self.test_string}</i>')

    def test_bold(self):
        @bold
        def return_str():
            return self.test_string

        self.assertEqual(return_str(), f'<b>{self.test_string}</b>')

    def test_underline(self):
        @underline
        def return_str():
            return self.test_string

        self.assertEqual(return_str(), f'<u>{self.test_string}</u>')

    def test_mixed(self):
        @italic
        @bold
        @underline
        def return_str():
            return self.test_string

        self.assertEqual(return_str(), f'<i><b><u>{self.test_string}</u></b></i>')

        @bold
        @italic
        @underline
        def return_str():
            return self.test_string

        self.assertEqual(return_str(), f'<b><i><u>{self.test_string}</u></i></b>')

        @underline
        @bold
        @italic
        def return_str():
            return self.test_string

        self.assertEqual(return_str(), f'<u><b><i>{self.test_string}</i></b></u>')

    def test_repeat(self):
        @italic
        @italic
        def return_str():
            return self.test_string

        self.assertEqual(return_str(), f'<i><i>{self.test_string}</i></i>')

        @italic
        @bold
        @italic
        def return_str():
            return self.test_string

        self.assertEqual(return_str(), f'<i><b><i>{self.test_string}</i></b></i>')
