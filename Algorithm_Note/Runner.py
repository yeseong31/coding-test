# 팰린드롬 연결 리스트
# 연결 리스트가 팰린드롬 구조인지 판별하라.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: ListNode) -> bool:
    # 런너
    rev = None
    slow = fast = None

    # 런너를 이용하여 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next      # 다중 할당
    if fast:
        slow = slow.next

    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        rev, slow = rev.next, slow.next
    return not rev      # return not slow 역시 가능함

# ---------------------------------------------------
# [런너를 이용한 우아한 풀이]
# 빠른 런너와 느린 런너를 각각 출발시킨 후, 빠른 런너가 끝에 다다를 때 느린 런너는 정확히 중간 지점에 도달하게끔 함
# 느린 런너는 중간까지 이동하면서 역순으로 연결 리스트 rev를 만들어 나감
# 중간에 도달한 느린 런너가 나머지 경로로 이동할 때, 역순으로 만든 연결 리스트의 값들과 일치하는지 확인해나가면 됨
