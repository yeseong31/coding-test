# 두 수의 덧셈(221p)
# 역순으로 저장된 연결 리스트의 숫자를 더하라.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 역순 리스트 만듦
    def reverse(self, l: ListNode):
        prev, cur = None, l
        while cur:
            next, cur.next = cur.next, prev
            prev, cur = cur, next
        return prev

    # 역순 연결 리스트를 리스트로 변환
    def toList(self, l: ListNode) -> list[int]:
        res = []
        while l:
            res.append(l.val)
            l = l.next
        return res

    # 리스트를 역순 연결 리스트로 변환
    def toReverseLinkedList(self, l: ListNode) -> ListNode:
        prev = None
        for i in l:
            node = ListNode(i, prev)
            prev = node
        return node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = self.toList(self.reverse(l1))
        n2 = self.toList(self.reverse(l2))
        res = int(''.join(str(e) for e in n1)) + int(''.join(str(e) for e in n2))
        return self.toReverseLinkedList(str(res))
