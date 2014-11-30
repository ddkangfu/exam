#coding=utf-8

import re
import math


def string_to_long(s):
    pattern = re.compile(r'^[+-]?[1-9]\d*|0$')
    if (not s) or (not s.strip()) or (not pattern.match(s.strip())):
        raise ValueError("invalid literal for string_to_long() with base 10: '%s'" % s)

    s = s.strip()
    rev_s = s[::-1]
    result = sum([int(math.pow(10, i)) * (ord(rev_s[i]) - ord('0')) for i in range(len(rev_s)) if rev_s[i] not in ['+', '-']])
    return (result * -1) if s[0] == '-' else result


if __name__ == '__main__':
    print string_to_long('1234567')
    print string_to_long('-5678')
    print string_to_long('+1189700')

