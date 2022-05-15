# k개 정렬 리스트 병합(274p)

import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: list[ListNode]) -> ListNode:
    q = []
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(q, (lists[i].val, i, lists[i]))

    root = result = ListNode(None)
    while q:
        now = heapq.heappop(q)
        result.next = now[2]
        result = result.next
        if result.next:
            heapq.heappush(q, (result.next.val, now[1], result.next))

    return root.next

