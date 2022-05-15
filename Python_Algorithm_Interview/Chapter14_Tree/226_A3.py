# 풀이 3 - 반복 구조로 DFS

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 어차피 연결 리스트로 되어 있어서 스택이든 큐이든 상관 없음... 속도는 스택 쪽이 좀 더 빠름
        stack = [root]

        while stack:
            node = stack.pop()

            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)

        return root
