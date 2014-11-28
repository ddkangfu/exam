#coding=utf-8

def string_to_long(s):
    if not s:
        return 0 #这里需要返回非法格式异常
    if not (s[0] == '+' or s[0] == '-' or (ord(s[0]) >=ord('0') and ord(s[0]) <= ord('9'))):
        return 0 #这里需要返回非法格式异常
    result = 0
    sign = 1
    for c in s:
        if c == '+':
            continue
        elif c == '-':
            sign = -1
            continue
        elif ord(c) >= ord('0') and ord(c)<= ord('9'):
            result = result * 10 + (ord(c) - ord('0'))
        else:
            return 0
    return result * sign

if __name__ == '__main__':
    print string_to_long('1234567')
    print string_to_long('-5678')
    print string_to_long('+1189700')

