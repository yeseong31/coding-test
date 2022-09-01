import sys
input = sys.stdin.readline

n = int(input())
# 회의 시간: 시간이 짧은 순 & 빨리 시작하는 순으로 정렬
meeting = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: (x[1], x[0]))

answer = 0
start = end = 0
for s, e in meeting:
    if s >= end:
        answer += 1
        end = e

print(answer)
