# Valid Sudoku
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_row(x):
            nums = set()
            for y in range(n):
                if board[x][y] == '.':
                    continue
                if board[x][y] in nums:
                    return False
                nums.add(board[x][y])
            return True

        def check_col(y):
            nums = set()
            for x in range(n):
                if board[x][y] == '.':
                    continue
                if board[x][y] in nums:
                    return False
                nums.add(board[x][y])
            return True

        def check_box(x, y):
            nums = set()
            for a in range(x, x + 3):
                for b in range(y, y + 3):
                    if board[a][b] == '.':
                        continue
                    if board[a][b] in nums:
                        return False
                    nums.add(board[a][b])
            return True

        n = 9
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                if not check_box(i, j):
                    return False
        for k in range(n):
            if not check_row(k) or not check_col(k):
                return False
        return True
