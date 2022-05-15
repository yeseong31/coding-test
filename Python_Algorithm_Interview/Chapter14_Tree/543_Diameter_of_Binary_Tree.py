# 이진 트리의 직경
# 이진 트리에서 두 노드 간 가장 긴 경로의 길이를 출력하라.

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    distance = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if not node:
                return -1

            # 왼쪽, 오른쪽 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            self.distance = max(self.distance, left + right + 2)
            return max(left, right) + 1

        dfs(root)
        return self.distance
