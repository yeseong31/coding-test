# 배낭 문제
# 배낭에 담을 수 있는 무게의 최댓값이 정해져 있고,
# 각각 짐의 가치와 무게가 있는 짐들을 배낭에 넣을 때 가치의 합이 최대가 되도록 짐을 고르는 문제

# ----------------------------------------------------------------------------------------------------------------------
# 분할 가능 배낭 문제

def fractional_knapsack(cargo):
    # 배낭에 담을 수 있는 무게의 최댓값
    capacity = 15
    # 새로운 배낭: 단가 계산 역순 정렬 -> [(10, 4), (2, 1), (2, 2), (1, 1), (4, 12)]
    pack = sorted(cargo, key=lambda x: (x[0] / x[1], x[0], x[1]), reverse=True)
    # 결괏값
    answer: float = 0

    # 단가가 제일 높은 순으로 그리디 계산
    for cost, weight in pack:
        # 최댓값 도달 전이라면 단가 순으로 담음
        if capacity - weight >= 0:
            capacity -= weight
            answer += cost
        # 남은 무게의 경우, 짐을 쪼개서 담음
        else:
            fraction = capacity / weight
            answer += fraction * cost
            break

    return answer


# 단가(1kg 당)가 가장 높은 짐부터 차례대로 선택
# C, B, E, D 선택 후 나머지 7kg를 담기 위해 A를 '7/12'만큼 쪼개서 '단가' 양만큼 담음
cargo = {
    (4, 12),  # A
    (2, 1),  # B
    (10, 4),  # C
    (1, 1),  # D
    (2, 2)  # E
}
r = fractional_knapsack(cargo)
print(r)
