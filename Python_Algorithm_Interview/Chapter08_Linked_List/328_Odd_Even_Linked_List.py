# 홀짝 연결 리스트(233p)
# 연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라.
# 공간 복잡도 O(1), 시간 복잡도 O(N)에 풀이하라.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        odd, even, root = head, head.next, head.next
        while odd and odd.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        odd.next = root
        return head
