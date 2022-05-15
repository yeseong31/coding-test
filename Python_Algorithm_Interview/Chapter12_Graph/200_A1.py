# 풀이 1 - DFS로 그래프 탐색

def numIslands(self, grid: list[list[str]]) -> int:
    def dfs(i: int, j: int):
        # 더 이상 땅이 아닌 경우 종료
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)

    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                # 모든 육지 탐색 후 카운트 1 증가
                cnt += 1

    return cnt
