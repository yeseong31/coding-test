import heapq


def solution(scoville, K):
    # 전체 원소가 k 이상인지 확인
    def check(q):
        for i in q:
            if i < K:
                return False
        return True

    q = []
    cnt = 0

    for s in scoville:
        heapq.heappush(q, s)

    while True:
        # 전체 원소가 k 이상이라면 return cnt
        if check(q):
            return cnt

        if len(q) < 2:
            return -1

        first = heapq.heappop(q)
        second = heapq.heappop(q)
        heapq.heappush(q, (first + second * 2))
        cnt += 1