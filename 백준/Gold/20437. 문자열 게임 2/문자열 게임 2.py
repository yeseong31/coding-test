import sys
from collections import defaultdict

input = sys.stdin.readline

for _ in range(int(input())):
    w = input().strip()
    k = int(input())
    count = defaultdict(list)
    
    for i in range(len(w)):
        if w.count(w[i]) >= k:
            count[w[i]].append(i)
            
    if not count:
        print(-1)
        continue
    
    mn, mx = 10000, 0
    for i in count:
        for j in range(len(count[i]) - k + 1):
            _len = count[i][j + k - 1] - count[i][j] + 1
            mn, mx = min(mn, _len), max(mx, _len)
    print(mn, mx)
