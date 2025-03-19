import sys
input = sys.stdin.readline

n, m = map(int, input().split())

str_set = {0, }
for _ in range(n):
    str_set.add(input())

cnt = 0
for _ in range(m):
    target = input()
    if target not in str_set:
        continue
    cnt += 1

print(cnt)