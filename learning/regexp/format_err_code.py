# -*- coding:utf8 -*-

import re


def extract_error_code(txt):
    result = re.match(r'^(.*)\("(.*?)",.*"(.*?)".*', txt)
    if result:
        name = result.group(1).strip()
        code = result.group(2).strip()
        desc = result.group(3).strip()
        return name, code, desc
    else:
        return None


def format(file, separator):
    formatted_text = []
    with open(file, 'rt', encoding='UTF-8') as f:
        line = f.readline()
        line_num = 1
        while line:
            info = extract_error_code(line)
            if info:
                formatted_text.append(separator.join(info))
            else:
                print('parse code error on row: %d, text: %s' %
                      (line_num, line))

            line = f.readline()
            line_num = line_num + 1

    return formatted_text
