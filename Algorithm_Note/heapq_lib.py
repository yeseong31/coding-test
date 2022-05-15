# 파이썬에서는 '힙' 기능을 위해 heapq 라이브러리를 제공한다.

# heapq
# - 다익스트라 최단 경로 알고리즘을 포함하여 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용된다.
# - 파이썬의 힙은 '최소 힙'으로 구성되어 있으므로 단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도
#   시간 복잡도 O(NlogN)에 오름차순 정렬이 완료된다.

# 원소 삽입: heapq.heappush() 메서드
# 원소 꺼냄: heapq.heappop() 메서드

import heapq

def minheap(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = minheap([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# 파이썬에서는 최대 힙을 제공하지 않는다.
# 최대 힙을 구현해야 할 때는 원소의 부호를 임시로 변경하는 방식을 사용한다.
# 힙에 원소를 삽입하기 전에 잠시 부호를 반대로 바꾸었다가, 힙에서 원소를 꺼낸 뒤에 다시 원소의 부호를 바꾸면 된다.

def maxheap(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = maxheap([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)