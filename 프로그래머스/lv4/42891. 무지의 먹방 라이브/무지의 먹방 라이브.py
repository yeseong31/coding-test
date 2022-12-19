from heapq import heapify, heappush, heappop


def solution(food_times, k):
    # 장애 전에 다 먹을 수 있다면 -1 반환
    if sum(food_times) <= k:
        return -1
    # 회전판(섭취 시간이 짧은 순으로 우선순위 큐 설정)
    q = [(v, i) for i, v in enumerate(food_times, 1)]
    heapify(q)
    # 이전에 섭취한 음식
    prev = 0
    
    # 섭취 시간 = (현재 음식 섭취 시간 - 이전 음식 섭취 시간(회전 횟수)) * 남은 음식 수
    while q and (q[0][0] - prev) * len(q) <= k:
        t = heappop(q)[0]
        k -= (t - prev) * (len(q) + 1)
        prev = t
    return sorted(q, key=lambda x: x[1])[k % len(q)][1]