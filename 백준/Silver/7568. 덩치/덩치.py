n = int(input())

data = []
for _ in range(n):
    a, b = map(int, input().split())
    data.append((a, b))

for i in data:
    rank = 1
    for j in data:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')
