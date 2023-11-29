a, b = map(int, input().split())
c = int(input())

h, m = divmod(b + c, 60)
print((a + h) % 24, m)