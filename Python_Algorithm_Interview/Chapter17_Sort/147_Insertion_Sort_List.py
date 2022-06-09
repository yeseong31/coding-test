"""
삽입 정렬 리스트(500p)
연결 리스트를 삽입 정렬로 정렬하라.
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = parent = ListNode()
        while head:
            # head를 움직이면서 cur보다 작은 값을 만날 때까지 반복
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            cur.next, head.next, head = head, cur.next, head.next

            # 즉시 되돌아가지 않고 계속 비교를 진행해도 되는지 확인
            # 이 코드의 추가로 실행 시간이 10배 이상 차이나게 됨
            if head and cur.val > head.val:
                cur = parent

        return parent.next
