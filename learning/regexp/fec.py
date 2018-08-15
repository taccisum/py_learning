# -*- coding:utf8 -*-

import sys
from format_err_code import format

if len(sys.argv) > 1:
    format(sys.argv[1])
else:
    print('please specify a file. exp: python fec.py "D:\\foo.txt"')