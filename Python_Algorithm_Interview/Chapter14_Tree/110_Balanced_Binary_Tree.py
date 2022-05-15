# 균형 이진 트리(413p)
# 이진 트리가 높이 균형인지 판단하라.
# 높이 균형은 모든 노드의 서브 트리 간의 높이 차이가 1 이하인 것을 말한다.

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    check = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 끝까지 간 다음 상태 저장 값 비교로 해결?
        def dfs(node):
            if node is None:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) >= 2:
                self.check = False

            return max(left, right) + 1

        dfs(root)
        return self.check
