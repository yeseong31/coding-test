# 풀이 2 - 반복 구조로 BFS
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = collections.deque([root])

        while q:
            node = q.popleft()

            # 부모 노드부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left
                q.append(node.left)
                q.append(node.right)

        return root
