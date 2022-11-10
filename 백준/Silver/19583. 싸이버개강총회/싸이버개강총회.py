import sys
from collections import defaultdict

input = sys.stdin.readline

answer = 0
s, e, q = input().split()
students = defaultdict(int)

while True:
    try:
        t, name = input().split()
        if t <= s:
            students[name] += 1
            continue
        if e <= t <= q and students[name]:
            students.pop(name)
            answer += 1
    except:
        break

print(answer)
