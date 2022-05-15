# 풀이 2 - 반복 구조로 뒤집기

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, node = None, head
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev
