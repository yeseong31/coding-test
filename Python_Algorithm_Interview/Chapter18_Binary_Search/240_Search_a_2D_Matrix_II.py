from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = len(matrix[0]) - 1, 0
        while 0 <= i and j < len(matrix):
            if matrix[j][i] == target:
                return True
            elif matrix[j][i] > target:
                i -= 1
            else:
                j += 1
        return False


# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         return any(target in row for row in matrix)
