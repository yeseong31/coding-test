from math import factorial

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(factorial(b) // (factorial(a) * factorial(b - a)))

