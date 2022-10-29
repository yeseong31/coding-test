def calcul_gcd(x, y):
    while True:
        div, mod = divmod(x, y)
        if mod == 0:
            return y
        x, y = y, mod


for _ in range(int(input())):
    a, b = map(int, input().split())
    gcd = calcul_gcd(a, b)
    result = gcd * (a // gcd) * (b // gcd)
    print(result)