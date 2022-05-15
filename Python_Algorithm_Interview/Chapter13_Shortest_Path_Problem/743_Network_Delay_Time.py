# 네트워크 딜레이 타임(373p)

# K부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산하라.
# 불가능한 경우 -1을 리턴한다.
# 입력값 (u, v, w)는 각각 출발지, 도착지, 소요 시간으로 구성되며, 전체 노드의 개수는 N으로 입력받는다.
import collections
import heapq

INF = int(1e9)


def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    dist = collections.defaultdict(int)
    q = [(0, k)]
    while q:
        time, node = heapq.heappop(q)
        if node not in dist:    # 값이 비어 있으면 '방문하지 않은 노드'
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(q, (alt, v))

    if len(dist) == n:
        return max(dist.values())
    return -1


times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(networkDelayTime(times, n, k))
# Output: 2

times = [[1,2,1]]
n = 2
k = 1
print(networkDelayTime(times, n, k))
# Output: 1

times = [[1,2,1]]
n = 2
k = 2
print(networkDelayTime(times, n, k))
# Output: -1
