import heapq
import sys
input = sys.stdin.readline


for _ in range(int(input())):
    k = int(input())
    max_h = []
    min_h = []
    visited = [False] * k

    for i in range(k):
        op, n = input().split()
        n = int(n)

        # 'I'라면 정수 n을 큐에 삽입
        if op == 'I':
            heapq.heappush(max_h, (-n, i))
            heapq.heappush(min_h, (n, i))
            visited[i] = True
        elif op == 'D':
            # 'D 1'이라면 큐에서 최댓값 삭제
            if n == 1:
                # visited를 이용하여 최소 힙과 동기화
                while max_h and not visited[max_h[0][1]]:
                    heapq.heappop(max_h)
                if max_h:
                    visited[max_h[0][1]] = False
                    heapq.heappop(max_h)
            # 'D -1'이라면 큐에서 최솟값 삭제
            else:
                # visited를 이용하여 최대 힙과 동기화
                while min_h and not visited[min_h[0][1]]:
                    heapq.heappop(min_h)
                if min_h:
                    visited[min_h[0][1]] = False
                    heapq.heappop(min_h)

    # 최대 힙과 최소 힙 동기화
    while max_h and not visited[max_h[0][1]]:
        heapq.heappop(max_h)
    while min_h and not visited[min_h[0][1]]:
        heapq.heappop(min_h)

    if not (min_h and max_h):
        print('EMPTY')
    else:
        print(-max_h[0][0], min_h[0][0])


# 시간 초과 풀이
# for _ in range(int(input())):
#     k = int(input())
#     ops = [(input().split()) for _ in range(k)]
#     q = []
#
#     # 최대 힙, 최소 힙 구성
#     for op, n in ops:
#         # 'I'라면 정수 n을 큐에 삽입
#         if op == 'I':
#             heapq.heappush(q, int(n))
#         elif q and op == 'D':
#             # 'D 1'이라면 큐에서 최댓값 삭제
#             if n == '1':
#                 q.pop(q.index(heapq.nsmallest(1, q)[0]))
#             # 'D -1'이라면 큐에서 최솟값 삭제
#             else:
#                 heapq.heappop(q)
#
#     if len(q) == 0:
#         print('EMPTY')
#     else:
#         print(heapq.nlargest(1, q)[0], q[0])

