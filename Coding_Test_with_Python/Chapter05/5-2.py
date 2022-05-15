# 파이썬으로 큐를 구현할 때는 collections 모듈에서 deque 자료구조를 활용하자.

from collections import deque
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

# deque 객체를 리스트 자료형으로 변경하고자 한다면 list() 메서드로 감싸주면 된다.
# 이 코드에서는 list(queue)를 하면 리스트 자료형이 반환된다.
