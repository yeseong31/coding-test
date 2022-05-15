# 팰린드롬 연결 리스트(201p)
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
런너 기법
- 연결 리스트를 순회할 때 2개의 포인터를 동시에 사용하는 기법
- 병합 지점, 중간 위치, 길이 등을 판별할 때 유용하게 사용
"""
def isPalindrome(head: ListNode) -> bool:
    # 빠른 런너 fast와 느린 런너 slow의 출발점은 같음
    rev = None
    slow = fast = head
    # next가 존재하지 않을 때까지 이동
    # 역순 연결 리스트 rev 생성도 같이 함
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    # 만약 fast가 남아 있다면 slow를 한 번 더 이동
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        rev, slow = rev.next, slow.next

    return not rev




head = ListNode([1,2,2,1])
print(isPalindrome(head))
