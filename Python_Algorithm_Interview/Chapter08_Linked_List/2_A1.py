# 풀이 1 - 자료형 변환

# Definition for singly-linked list.
import functools
from operator import add


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

    # 연결 리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode) -> ListNode:
        lst: list = []
        while node:
            lst.append(node.val)
            node = node.next
        return lst

    # 파이썬 리스트를 역순 연결 리스트로 변환
    def toReverseLinkedList(self, res: ListNode) -> ListNode:
        prev: ListNode = None
        for r in res:
            node = ListNode(r, prev)
            prev = node
        return node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        # result = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
        result = functools.reduce(add, a) + functools.reduce(add, b)
        return self.toReverseLinkedList(result)
