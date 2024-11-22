n = int(input())
lst = list(map(int, input().split()))
lst.reverse()

# d[i]: lst[i]를 마지막 원소로 가지는 부분 수열의 최댓값
d = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if lst[i] > lst[j]:
            d[i] = max(d[i], d[j] + 1)

print(n - max(d))