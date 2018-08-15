# -*- coding:utf8 -*-

import os
import sys
import getopt
from format_err_code import format


def usage():
    with open('help.txt', 'rt', encoding='utf8') as f:
        line = f.readline()
        while line:
            print(line)
            line = f.readline()


def do_verbose(verbose, text_ls):
    if verbose:
        print('formatted text:')
        for t in text_ls:
            print(t)


def do_out(out, text_ls):
    if out:
        with open(out, 'wt', encoding='utf8') as f_out:
            if f_out.writable():
                for t in formatted_text:
                    f_out.write(t)
                    f_out.write(os.linesep)
            else:
                print('can not write file to out.txt')


def gopt(argv):
    try:
        return getopt.getopt(argv[1:], 'hvs:o:', ['help', 'verbose', 'separator=', 'out='],)
    except getopt.GetoptError as e:
        print('error args')
        usage()
        sys.exit()


if __name__ == '__main__':
    file_path = None
    separator = ','
    out = 'out.txt'
    verbose = False

    opts, args = gopt(sys.argv)
    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
            sys.exit(1)
        if o in ('-s', '--separator'):
            separator = a
        if o in ('-o', '--out'):
            out = a
        if o in ('-v', '--verbose'):
            verbose = True

    if len(args) == 0:
        print('please specify a file.')
        usage()
        sys.exit()
    elif len(args) > 1:
        print('more than one arg')
        usage()
        sys.exit()


    file_path = args[0]

    if verbose:
        print('file: %s, separator: %s, out: %s' % (file_path, separator, out))

    formatted_text = format(file_path, separator)
    do_verbose(verbose, formatted_text)
    do_out(out, formatted_text)
