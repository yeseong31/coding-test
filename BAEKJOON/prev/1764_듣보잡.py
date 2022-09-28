import sys
input = sys.stdin.readline

n, m = map(int, input().split())

check_set = set()
for _ in range(n):
    check_set.add(input())

answer = []
for _ in range(m):
    target = input()
    if target in check_set:
        answer.append(target)

print(len(answer))
for s in sorted(answer):
    print(s, end='')
