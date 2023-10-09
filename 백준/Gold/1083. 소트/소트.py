import sys

n = int(input())
ans = list(map(int, sys.stdin.readline().split()))
s = int(input())

for x in range(n - 1):
    if s == 0:
        break
    
    mx, t = ans[x], 0
    
    for y in range(x + 1, n):
        if mx < ans[y]:
            mx = ans[y]
            t = y - x
        if y - x >= s:
            break
    
    if t:
        s -= t
        ans.remove(mx)
        ans.insert(x, mx)

print(*ans)
