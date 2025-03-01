def check(x1, y1, x2, y2):
    ans = 0
    for i in range(x1, x2):
        for j in range(y1, y2):
            if area[i][j] == 0:
                area[i][j] = 1
                ans += 1
    return ans


area = [[0] * 100 for _ in range(100)]
result = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    result += check(x1, y1, x2, y2)

print(result)