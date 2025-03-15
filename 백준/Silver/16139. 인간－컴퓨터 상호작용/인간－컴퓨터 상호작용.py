import string
import sys

s = input()
n = int(input())
length = len(s)

alphabets = {}
for c in string.ascii_lowercase:
    alphabets[c] = [0]
    cnt = 0
    for i in range(length):
        if s[i] == c:
            cnt += 1
        alphabets[c].append(cnt)

for _ in range(n):
    tmp = sys.stdin.readline().rstrip().split()
    a, l, r = tmp[0], int(tmp[1]), int(tmp[2])
    print(alphabets[a][r + 1] - alphabets[a][l])