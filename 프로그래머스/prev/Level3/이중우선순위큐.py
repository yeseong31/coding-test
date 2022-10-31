import heapq


def solution(operations):
    q1, q2 = [], []
    length = 0

    for operation in operations:
        op, n = operation.split()
        # 숫자 삽입
        if op == 'I':
            heapq.heappush(q1, int(n))
            length += 1
        elif length > 0:
            # 최댓값 삭제
            if n == '1':
                q2 = heapq.nlargest(len(q1), q1)
                heapq.heappop(q2)
                q1 = q2
            # 최솟값 삭제
            else:
                heapq.heappop(q1)
            length -= 1

    if length == 0:
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
