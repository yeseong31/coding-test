import heapq


# 음식 섭취 시 필요한 시간 배열 food_times, 방송이 중단된 시간 k
def solution(food_times, k):
    # 남은 시간 안에 더 섭취할 음식이 없다면 return -1
    if sum(food_times) <= k:
        return -1

    n = len(food_times)
    q = []
    for i in range(n):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_times = 0
    prev = 0

    while sum_times + (q[0][0] - prev) <= k:
        now = heapq.heappop(q)[0]
        sum_times += (now - prev) * n
        prev = now
        n -= 1

    # 남은 음식들 재정렬
    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_times) % n][1]


food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))
