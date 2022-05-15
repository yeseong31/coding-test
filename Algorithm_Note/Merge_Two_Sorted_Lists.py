# 두 정렬 리스트의 병합
# 정렬되어 있는 두 연결 리스트를 합쳐라

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1

# ---------------------------------------------------------------------
# [재귀 구조로 연결]
# 져기서는, 정렬된 리스트라는 점이 중요함
# 즉 병합 정렬에서 마지막 조합 시 첫 번째 값부터 차례대로만 비교하면 한 번에 해결되듯이,
# 이 또한 병합 정렬의 마지막 조합과 동일한 방식으로 첫 번째부터 비교하면서 리턴하면 쉽게 풀 수 있는 문제임

# l1과 l2의 값을 비교하여 작은 값이 왼쪽에 오게 하고, next는 그다음 값이 엮이도록 진행
# 마지막에는 l1이 null이 됨녀서 재귀가끝나고 리턴 시작 (백트래킹)
