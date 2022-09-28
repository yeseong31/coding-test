# 물품의 수, 무게
n, k = map(int, input().split())
# 물건, 가치
w_list, v_list = [0], [0]
for _ in range(n):
    a, b = map(int, input().split())
    w_list.append(a)
    v_list.append(b)

# 냅색
knapsack = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w, v = w_list[i], v_list[i]

        if j < w:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(knapsack[i - 1][j - w_list[i]] + v_list[i], knapsack[i - 1][j])

print(knapsack[n][k])
