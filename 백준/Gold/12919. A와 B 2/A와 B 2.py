import sys
input = sys.stdin.readline


def check(t):
    if len(s) == len(t):
        return s == t
    if t[0] == 'B' and check(t[:0:-1]):
        return True
    return t[-1] == 'A' and check(t[:-1])


s = input().strip()
print(1 if check(input().strip()) else 0)
