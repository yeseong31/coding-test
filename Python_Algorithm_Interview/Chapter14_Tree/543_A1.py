# 풀이 1 - 상태값 누적 트리 DFS

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    distance: int = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            # 상태값 = 리프 노드에서 현재 노드까지의 거리
            # 직경 = 왼쪽 자식 노드의 상태값 + 오른쪽 자식 노드의 상태값 + 2
            self.distance = max(self.distance, left + right + 2)
            return max(left, right) + 1

        dfs(root)
        return self.distance
