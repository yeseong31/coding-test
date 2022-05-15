# 최소 높이 트리(416p)
# 노드 개수와 무방향 그래프를 입력받아 트리가 최소 높이가 되는 루트의 목록을 리턴하라.
import collections
from typing import List


class Solution:
    result = []

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def bfs(v):
            depth = -1
            s = set()
            s.add(v)
            q = collections.deque([v])

            while q:
                depth += 1
                for _ in range(len(q)):
                    node = q.popleft()
                    for i in graph[node]:
                        if i not in s:
                            q.append(i)
                            s.add(i)

            self.result.append((v, depth))

        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # 하나씩 출발지 설정... 최대 높이 확인
        for start in graph.keys():
            bfs(start)

        length = sorted(self.result, key=lambda x: x[1])[0][1]

        return [a for a, b in self.result if b == length]


solution = Solution()

n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
print(solution.findMinHeightTrees(n, edges))

# 파이참에서는 맞는데 왜 leetcode에서는 틀리지?

# Input: n = 4, edges = [[1,0],[1,2],[1,3]]
# Output: [1]

# Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# Output: [3,4]

# Input: n = 1, edges = []
# Output: [0]

# Input: n = 2, edges = [[0,1]]
# Output: [0,1]
