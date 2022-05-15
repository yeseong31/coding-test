# 두 수의 덧셈
# 역순으로 저장된 연결 리스트의 숫자를 더하라
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)      342 + 465
# Output: 7 -> 0 -> 8                           = 807

# 연산 결과로 나머지를 취하고 몫은 자리올림수 형태로 올리는 전가산기의 전체 구조만 참고하여 풀이함
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry, val = divmod(sum + carry, 10)    # 몫과 나머지로 구성된 튜플 리턴
            head.next = ListNode(val)
            head = head.next

        return root.next