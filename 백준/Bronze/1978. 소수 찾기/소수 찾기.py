n = int(input())
data = list(map(int, input().split()))
count = 0
for d in data:
    cnt = 0
    if d == 1:
        continue
    for i in range(2, d + 1):
        if d % i ==0:
            cnt += 1
    if cnt == 1:
        count += 1
print(count)