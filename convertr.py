#coding=utf-8


def string_to_long(s):
    if not s:
        return 0 #这里需要返回非法格式异常
    if not (s[0] == '+' or s[0] == '-' or (s[0] >=ord('0') and  s[0] <= ord('9'))):
        return 0 #这里需要返回非法格式异常
    result = 1
    for c in s:
        if c == '+':
            continue
        elif c == '-':
            result *= -1
            continue
        elif c >= ord('0') and c<= ord('9'):
            result = result * 10 + (ord(c) - ord('0'))
        else:
            return 0
    return result

if __name__ == '__main__':
    print string_to_long('1234567')

