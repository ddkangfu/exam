#coding=utf-8

import re
import math


def string_to_long(s):
    s = s.strip()
    pattern = re.compile(r'^[+-]?[1-9]\d*|0$')

    if (not s) or (not pattern.match(s)):
        return 0 #这里需要返回非法格式异常

    rev_s = s[::-1]
    result = sum([int(math.pow(10, i)) * (ord(rev_s[i]) - ord('0')) for i in range(len(rev_s)) if rev_s[i] not in ['+', '-']])
    return (result * -1) if s[0] == '-' else result


if __name__ == '__main__':
    print string_to_long('1234567')
    print string_to_long('-5678')
    print string_to_long('+1189700')

