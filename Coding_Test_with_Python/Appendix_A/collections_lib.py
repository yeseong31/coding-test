# 파이썬의 collections 라이브러리는 유용한 자료구조를 제공하는 표준 라이브러리이다.

# ----------------------------------------------------------------------------------------
# deque
# 파이썬에서는 deque를 사용하여 큐를 구현한다.
# 별도로 제공되는 Queue 라이브러리가 있지만 이는 일반적인 큐 자료구조를 구현하는 라이브러리가 아님.

# 기본 리스트 자료형에서 앞쪽에 있는 원소를 삭제하거나 앞쪽에 새 원소를 삽입할 때의 시간 복잡도는 O(N)이지만
# deque의 경우 O(1)로 훨씬 성능이 좋다.
# 다만 deque에서는 리스트 자료형과 다르게 인덱싱, 슬라이싱 기능은 사용할 수 없다.

# popleft(): 첫 번째 원소 제거
# pop(): 마지막 원소 제거
# appendleft(x): 첫 번째 인덱스에 원소 x 삽입
# append(x): 마지막 인덱스에 원소 x 삽입

from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))

# ----------------------------------------------------------------------------------------
# Counter
# 등장 횟수를 세는 기능
# iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지를 알려준다.

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))