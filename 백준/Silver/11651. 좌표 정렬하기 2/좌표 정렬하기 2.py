import sys
input = sys.stdin.readline

data = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    data.append((a, b))

data.sort(key=lambda x: (x[1], x[0]))

for a, b in data:
    print(a, b)