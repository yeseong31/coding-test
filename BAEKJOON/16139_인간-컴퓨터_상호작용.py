# 특정 문자열 s, 특정 알파벳 a, 문자열의 구간 [l, r]

import sys
input = sys.stdin.readline

s = input()
n = int(input())

point = []
for alpha in 'abcdefghijklmnopqrstuvwxyz':
    count = 0
    tmp = []
    for c in str(s):
        if alpha == c:
            count += 1
        tmp.append(count)
    point.append(tmp)

for _ in range(n):
    a, l, r = input().split()
    target = point[ord(a) - ord('a')]
    ans = target[int(r)] - target[int(l)]

    if s[int(l)] == a:
        ans += 1
    print(str(ans))
