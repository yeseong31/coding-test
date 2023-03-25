from collections import defaultdict


def solution(info, edges):
    def dfs(cur, sheep, wolf, path):
        # XOR 연산으로 if문 없이 양, 늑대 정보 판단
        sheep += info[cur] ^ 1
        wolf += info[cur]
        # DFS 진행 조건
        if sheep <= wolf:
            return
        answer.append(sheep)
        # 다음 탐색 범위 계산
        # 이진 트리에서 나아갈 수 있는 모든 길에 대해 재귀 호출
        for p in path:
            tmp = set(graph.get(p, []))
            path |= tmp
            path -= set([p])
            dfs(p, sheep, wolf, path)
            path |= set([p])
            path -= tmp
    
    
    answer = []
    graph = defaultdict(list)
    for p, c in edges:
        graph[p].append(c)
        
    dfs(0, 0, 0, set(graph.get(0)))
    return max(answer)