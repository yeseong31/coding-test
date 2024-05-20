import sys
import heapq

input = sys.stdin.readline


q = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, x)