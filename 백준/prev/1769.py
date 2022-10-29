# 3의 배수

x = input()

count = 0
while len(x) > 1:
    count += 1
    _sum = 0
    for c in x:
        _sum += int(c)
    x = str(_sum)

print(count)
if int(x) % 3 == 0:
    print('YES')
else:
    print('NO')
