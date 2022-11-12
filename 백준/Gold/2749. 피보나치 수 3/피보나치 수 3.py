m = 1000000
p = 1500000
n = int(input()) % p

a = b = 1
for i in range(n - 2):
    a, b = b % m, (a + b) % m
print(b)