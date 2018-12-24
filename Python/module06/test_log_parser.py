import os
import re

from log_parser import LogParser
from unittest import TestCase


class TestLogParser(TestCase):
    def setUp(self):
        self.log_parser = LogParser('access.log')

    def tearDown(self):
        pass

    def test_get_most_common(self):
        self.assertEqual(self.log_parser.get_most_common(10),
                         [('198.50.156.189', 167812), ('5.112.235.245', 166722), ('5.114.231.216', 158258),
                          ('5.113.18.208', 157674), ('91.218.225.68', 134376), ('79.62.229.212', 114799),
                          ('149.56.83.40', 97533), ('5.114.64.184', 94043), ('5.113.216.211', 89125),
                          ('158.69.5.181', 88875)])
        self.assertEqual(self.log_parser.get_most_common(1), [('198.50.156.189', 167812)])

    def test_log_by_http_code(self):
        file_name = "access_404"
        pattern = re.compile(r'\s[\d]{3}\s')
        try:
            self.log_parser.log_by_http_code(file_name, 404)
            self.assertTrue(os.path.exists(file_name))
            with open(file_name, "r") as r_log:
                for line in r_log:
                    match = pattern.search(line)
                    if match == "":
                        self.fail()

        finally:
            os.remove(file_name)
