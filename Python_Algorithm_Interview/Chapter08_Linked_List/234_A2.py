# 풀이 2 - 데크를 이용한 최적화

from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: ListNode) -> bool:
    if not head:
        return True

    q = deque()
    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    return True


head = ListNode([1,2,2,1])
print(isPalindrome(head))
