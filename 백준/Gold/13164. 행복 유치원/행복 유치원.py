n, k = map(int, input().split())
s = list(map(int, input().split()))
print(sum(sorted([s[i] - s[i - 1] for i in range(1, n)], reverse=True)[k - 1:]))
