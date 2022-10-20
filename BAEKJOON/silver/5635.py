# 생일

answer = []

for _ in range(int(input())):
    answer.append(input().split())
answer.sort(key=lambda x: (int(x[3]), int(x[2]), int(x[1]), x[0]))

print(answer[-1][0])
print(answer[0][0])
