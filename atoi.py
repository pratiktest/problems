import sys

def atoi(s):
    res = 0
    sign = None
    for i in range(0, len(s)):
        if s[i] == '-' or s[i] =='+':
            sign = '-'
            continue
        if ord(s[i]) < ord('0') or ord(s[i]) > ord('9'):
            break
        res = res*10 + ord(s[i]) - ord('0')

    if sign == '-':
        res = res*-1

    """ in java keep this as double so we can fit an int"""
    if res < -2147483648:
        return -2147483648



    return res

if __name__ == '__main__':
    s = "2323"
    print(atoi(s))