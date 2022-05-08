# dp 테이블
d = [0] * 41
d[1] = 1
d[2] = 1

# 테스트 케이스의 개수 t
t = int(input())
for _ in range(t):
    n = int(input())
    if n == 0:
        print(f'{1} {0}')
        continue
    elif n == 1:
        print(f'{0} {1}')
        continue
    else:
        i = 3
        while i < n + 1:
            d[i] = d[i - 1] + d[i - 2]
            i += 1
        print(d[i - 2], d[i - 1])
