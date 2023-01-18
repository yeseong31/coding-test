import sys

input = sys.stdin.readline


def dfs(A, B, num):
    A.add(num)
    B.add(board[num])

    # graph[num]이 첫 번째 집합 A에 있다면
    if board[num] in A:
        # 결과 반영 후 종료
        if A == B:
            result.update(A)
    else:
        return dfs(A, B, board[num])


n = int(input())
board = [0] + [int(input()) for _ in range(n)]
result = set()

for i in range(1, n + 1):
    if i not in result:
        dfs(set(), set(), i)

print(len(result))
print(*sorted(list(result)), sep='\n')