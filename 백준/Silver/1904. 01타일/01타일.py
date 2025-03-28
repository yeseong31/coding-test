import sys
input = sys.stdin.readline

n = int(input())
ans = [0, 1, 2]

for k in range(3, n + 1):
    ans[0], ans[1], ans[2] = ans[1], ans[2], (ans[1] + ans[2]) % 15746

if n <= 2:
    print(n)
else:
    print(ans[2])