# 풀이 1 - 우선순위 큐를 이용한 리스트 병합
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        q = []
        root = result = ListNode(0)
        # 각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(q, (lists[i].val, i, lists[i]))
        # 힙 추출 이후 다음 노드는 다시 저장
        while q:
            node = heapq.heappop(q)
            idx = node[1]
            result.next = node[2]
            result = result.next
            if result.next:
                heapq.heappush(q, (result.next.val, idx, result.next))
        return root.next
