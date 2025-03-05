def calcul(x, y):
    while True:
        if (mod := x % y) == 0:
            return y
        x, y = y, mod


n = int(input())
rings = list(map(int, input().split()))

standard = rings[0]
for v in rings[1:]:
    gcd = calcul(standard, v)
    print(f'{standard // gcd}/{v // gcd}')
