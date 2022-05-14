# 특정 문자열 s, 특정 알파벳 a, 문자열의 구간 [l, r]

import sys
input = sys.stdin.readline
print = sys.stdout.write

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
    tmp = input().split()
    a, l, r = tmp[0], int(tmp[1]), int(tmp[2])
    target = point[ord(a) - ord('a')]
    ans = target[r] - target[l]

    if s[l] == a:
        ans += 1
    print(str(ans) + '\n')
