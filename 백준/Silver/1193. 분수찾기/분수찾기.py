x = int(input())

prev, n = 1, 2
while x > prev + n:
    prev += n
    n += 1

b = x - prev
a = n + 1 - b
if n % 2 == 0:
    a, b = b, a
if x == 1:
    a = b = 1
print('{}/{}'.format(a, b))