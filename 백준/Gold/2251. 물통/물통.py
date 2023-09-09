import sys
from collections import deque

input = sys.stdin.readline


def pour(cup_a, cup_b):
    if not visited[cup_a][cup_b]:
        visited[cup_a][cup_b] = True
        q.append((cup_a, cup_b))


answer = set()
size_a, size_b, size_c = map(int, input().split())

q = deque([(0, 0)])

visited = [[False] * (size_b + 1) for _ in range(size_a + 1)]
visited[0][0] = True

while q:
    volume_a, volume_b = q.popleft()
    volume_c = size_c - volume_a - volume_b
    
    if volume_a == 0:
        answer.add(volume_c)
    
    # A to B
    water = min(volume_a, size_b - volume_b)
    pour(volume_a - water, volume_b + water)
    # A to C
    water = min(volume_a, size_c - volume_c)
    pour(volume_a - water, volume_b)
    # B to A
    water = min(volume_b, size_a - volume_a)
    pour(volume_a + water, volume_b - water)
    # B to C
    water = min(volume_b, size_c - volume_c)
    pour(volume_a, volume_b - water)
    # C to A
    water = min(volume_c, size_a - volume_a)
    pour(volume_a + water, volume_b)
    # C to B
    water = min(volume_c, size_b - volume_b)
    pour(volume_a, volume_b + water)
    
print(*sorted(answer))