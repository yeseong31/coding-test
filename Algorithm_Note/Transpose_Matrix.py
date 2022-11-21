# 행렬 Transpose
def transpose_matrix():
    return [x for x in zip(*board)]


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
new_board = transpose_matrix()

for b in new_board:
    print(*b)

# Input
# 6
# 0 1 2 3 4 5
# 1 0 2 3 4 5
# 1 2 0 3 4 5
# 1 2 3 0 4 5
# 1 2 3 4 0 5
# 1 2 3 4 5 0

# Output
# 0 1 1 1 1 1
# 1 0 2 2 2 2
# 2 2 0 3 3 3
# 3 3 3 0 4 4
# 4 4 4 4 0 5
# 5 5 5 5 5 0
