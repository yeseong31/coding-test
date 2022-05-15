# 풀이 4 - 런너를 이용한 우아한 풀이

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: ListNode) -> bool:
    rev = None          # 역순 연결 리스트
    slow = fast = head  # 느린 런너, 빠른 런너

    # 런너를 이용하여 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:    # 입력값이 홀수일 때 slow 런너가 한 칸 더 앞으로 이동
        slow = slow.next

    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev


head = ListNode([1,2,2,1])
print(isPalindrome(head))
