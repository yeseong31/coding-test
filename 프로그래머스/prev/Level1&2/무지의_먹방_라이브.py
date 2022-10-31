import heapq

def solution(food_times, k):
    # 남은 음식이 없다면 -1 반환
    if sum(food_times) <= k:
        return -1

    n = len(food_times)
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    total = 0
    prev = 0

    while total + (q[0][0] - prev) * n <= k:
        now = heapq.heappop(q)[0]
        total += (now - prev) * n
        n -= 1
        prev = now

    # 남은 음식들 재정렬
    result = sorted(q, key=lambda x: x[1])
    return result[(k - total) % n][1]