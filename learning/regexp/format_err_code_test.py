# -*- coding:utf8 -*-

import unittest

from format_err_code import *


class TestFormatErrCode(unittest.TestCase):

    def test_extract_error_code(self):
        info = extract_error_code('EXPORT("11000", "export exception")')
        self.assertIsNotNone(info)
        self.assertEqual('EXPORT', info[0])
        self.assertEqual('11000', info[1])
        self.assertEqual('export exception', info[2])

    def test_extract_error_code_when_end_with_comma(self):
        info = extract_error_code('EXPORT("11000", "export exception"),')
        self.assertIsNotNone(info)
        self.assertEqual('EXPORT', info[0])
        self.assertEqual('11000', info[1])
        self.assertEqual('export exception', info[2])

    def test_extract_error_code_when_end_with_semicolon(self):
        info = extract_error_code('EXPORT("11000", "export exception" );')
        self.assertIsNotNone(info)
        self.assertEqual('EXPORT', info[0])
        self.assertEqual('11000', info[1])
        self.assertEqual('export exception', info[2])

    def test_extract_error_code_when_contain_blank(self):
        info = extract_error_code(
            '   EXPORT (" 11000 ", " export exception " )')
        self.assertIsNotNone(info)
        self.assertEqual('EXPORT', info[0])
        self.assertEqual('11000', info[1])
        self.assertEqual('export exception', info[2])

    def test_extract_error_code_when_format_error(self):
        info = extract_error_code('123')
        self.assertIsNone(info)

    def test_format(self):
        format('learning/regexp/ex.txt')


if __name__ == '__main__':
    unittest.main()
