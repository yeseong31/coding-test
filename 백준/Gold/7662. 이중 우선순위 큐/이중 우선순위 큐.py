import heapq
import sys
input = sys.stdin.readline


for _ in range(int(input())):
    max_h = []
    min_h = []
    visited = [False] * 1000001

    for i in range(int(input())):
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
                while max_h and not visited[max_h[0][1]]:
                    heapq.heappop(max_h)
                if max_h:
                    visited[max_h[0][1]] = False
                    heapq.heappop(max_h)
            # 'D -1'이라면 큐에서 최솟값 삭제
            else:
                while min_h and not visited[min_h[0][1]]:
                    heapq.heappop(min_h)
                if min_h:
                    visited[min_h[0][1]] = False
                    heapq.heappop(min_h)

    while max_h and not visited[max_h[0][1]]:
        heapq.heappop(max_h)
    while min_h and not visited[min_h[0][1]]:
        heapq.heappop(min_h)

    if not (min_h and max_h):
        print('EMPTY')
    else:
        print(-max_h[0][0], min_h[0][0])