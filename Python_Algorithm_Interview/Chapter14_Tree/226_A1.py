# 풀이 1 - 파이썬다운 방식
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        # return None

# 이 풀이에서는 오른쪽부터 재귀 탐색을 진행한다. self.invertTree의 파라미터로 root.right를 먼저 넘겼기 때문이다.
# 오른쪽 노드가 다 스윕된 이후에는 왼쪽 노드가 동일한 형태로 스왑된다.
# 참고로 마지막 return None은 생략이 가능하다. 아무것도 리텀하지 않으면 자바나 C++는 당연히
# 에러를 내겠지만, 파이썬은 자연스럽게 None을 할당하기 때문이다. (동적 타이핑 덕분)
