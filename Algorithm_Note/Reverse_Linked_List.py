# 역순 연결 리스트
# 연결리스트를 뒤집어라

# 풀이 1 - 재귀 구조로 뒤집기

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None) -> ListNode:
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)

# -------------------------------------------------------------------------
# 풀이 2 - 반복 구조로 뒤집기


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, node = None, head
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

# 역순 연결 리스트 II
# 인덱스 m에서 n까지를 역순으로 만들어라. 인덱스 m은 1부터 시작한다.

# 풀이 1 - 반복 구조로 노드 뒤집기


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head

        root = start = ListNode(0)
        root.next = head
        for _ in range(left - 1):
            start = start.next
        end = start.next

        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp

        return root.next
