"""
리스트 정렬(489p)
연결 리스트를 O(n log n)에 정렬하라
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        lst = []

        # linked list to python list
        while p:
            lst.append(p.val)
            p = p.next

        lst.sort()

        # python list to linked list
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head


# 병합 정렬 ver
# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         if l1 and l2:
#             if l1.val > l2.val:
#                 l1, l2 = l2, l1
#             l1.next = self.mergeTwoLists(l1.next, l2)
#         return l1 or l2
#
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not (head and head.next):
#             return head
#
#         # 입력이 리스트이므로 '중앙값'을 찾기 위해 '런너'를 활용
#         half, slow, fast = None, head, head
#         while fast and fast.next:
#             half, slow, fast = slow, slow.next, fast.next.next
#         half.next = None
#
#         l1 = self.sortList(head)
#         l2 = self.sortList(slow)
#
#         return self.mergeTwoLists(l1, l2)


