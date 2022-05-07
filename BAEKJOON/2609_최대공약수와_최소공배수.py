import math


def gcd(x, y):
    while True:
        div, mod = divmod(x, y)
        if mod == 0:
            return y
        x, y = y, mod


a, b = map(int, input().split())
gcd = gcd(a, b)
lcm = gcd * (a // gcd) * (b // gcd)

print(gcd)
print(lcm)
