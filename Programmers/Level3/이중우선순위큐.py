import heapq


def solution(operations):
    q1 = []
    p = 0
    for target in  operations:
        op, n = target.split()
        n = int(n)
        # 숫자 삽입
        if op == 'I':
            heapq.heappush(q1, n)
            p += 1
        elif p > 0 and op == 'D':
            # 최댓값 삭제
            if n == 1:
                q2 = heapq.nlargest(len(q1), q1)
                heapq.heappop(q2)
                q1 = q2
            # 최솟값 삭제
            elif n == -1:
                heapq.heappop(q1)
            p -= 1

    if p == 0:
        return [0, 0]
    return [*heapq.nlargest(1, q1), heapq.heappop(q1)]


# I 숫자: 큐에 숫자 삽입
# D 1: 큐에서 최댓값 삭제
# D -1: 큐에서 최솟값 삭제
# 모든 연산 이후 큐가 비어 있으면 [0, 0], 아니면 [최댓값, 최솟값] return

operations = ["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]
print(solution(operations))

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))
