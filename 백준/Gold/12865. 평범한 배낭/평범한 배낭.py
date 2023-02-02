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
    # 현재 배낭의 허용 무게 j
    for j in range(1, k + 1):
        w, v = w_list[i], v_list[i]

        # 현재 배낭의 허용 무게보다 넣을 물건의 무게가 더 크다면 넣지 않는다.
        if j < w:
            knapsack[i][j] = knapsack[i - 1][j]
        # 그렇지 않다면
        # 1) 현재 넣을 물건의 무게만큼 배낭에서 빼고 현재 물건을 넣는다.
        # 2) 현재 물건을 넣지 않고 이전의 배낭을 그대로 가져간다.
        else:
            knapsack[i][j] = max(knapsack[i - 1][j - w_list[i]] + v_list[i], knapsack[i - 1][j])

print(knapsack[n][k])