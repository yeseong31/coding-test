import heapq


def solution(operations):
    q1, q2 = [], []
    cnt = 0
    for operation in operations:
        op, n = operation.split()
        n = int(n)
        if op == 'I':
            heapq.heappush(q1, n)
            cnt += 1
        elif op == 'D' and cnt > 0:
            if n == 1:
                q2 = heapq.nlargest(len(q1), q1)
                heapq.heappop(q2)
                q1 = q2
            elif n == -1:
                heapq.heappop(q1)
            cnt -= 1

    if cnt == 0:
        return [0, 0]
    return [max(q1), min(q1)]
