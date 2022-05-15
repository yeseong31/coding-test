# 풀이 1 - 리스트 변환

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: ListNode) -> bool:
    if not head:
        return True

    q = []
    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
    return True


head = ListNode([1,2,2,1])
print(isPalindrome(head))
