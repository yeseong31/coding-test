"""
Q35 못생긴 수(381p)
"""

n = int(input())

d = [False] * 1001
d[1] = True

i = 0
cnt = 0
while True:
    i += 1
    # i가 가리키는 수가 '못생긴 수'가 아니라면 continue
    if not d[i]:
        continue
    cnt += 1
    if cnt == n:
        print(i)
        break
    # 못생긴 수에 대해 2, 3, 5를 곱한 수 역시 못생긴 수
    d[i * 2] = d[i * 3] = d[i * 5] = True
