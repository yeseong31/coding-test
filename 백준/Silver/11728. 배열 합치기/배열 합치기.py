from heapq import heapify, heappop

n, m = map(int, input().split())

result = []
for a in list(map(int, input().split())):
    result.append(a)
for b in list(map(int, input().split())):
    result.append(b)

heapify(result)
while result:
    print(heappop(result), end=' ')