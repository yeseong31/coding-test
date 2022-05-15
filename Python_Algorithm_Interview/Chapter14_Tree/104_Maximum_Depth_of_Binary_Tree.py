# 이진 트리의 최대 깊이(387p)

# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        q = deque([root])
        depth = 0

        while q:
            depth += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return depth


# Input: root = [3,9,20,null,null,15,7]             3
# Output: 3                                        / \
#                                                 9   20
# Input: root = [1,null,2]                            / \
# Output: 2                                          15  7
#
# Input: root = []
# Output: 0
#
# Input: root = [0]
# Output: 1
