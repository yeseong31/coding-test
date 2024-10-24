n = int(input())
p = sorted(list(map(int, input().split())))

answer = p[0]
for i in range(1, n):
    p[i] += p[i - 1]
    answer += p[i]
print(answer)