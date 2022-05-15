# 원형 데크 디자인(268p)

class MyCircularDeque:

    class ListNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def __init__(self, k: int):
        self.head = self.ListNode(None)
        self.tail = self.ListNode(None)
        self.k = k      # 원형 데크 크기 지정
        self.len = 0    # 현재 원형 데크 길이
        self.head.right = self.tail
        self.tail.left = self.head

    def insertFront(self, value: int) -> bool:
        if self.len >= self.k:
            return False
        node = self.ListNode(value)
        self.len += 1
        self.head.right.left = node
        node.right = self.head.right
        self.head.right = node
        node.left = self.head
        return True

    def insertLast(self, value: int) -> bool:
        if self.len >= self.k:
            return False
        self.len += 1
        node = self.ListNode(value)
        self.tail.left.right = node
        node.left = self.tail.left
        self.tail.left = node
        node.right = self.tail
        return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        target = self.head.right
        self.head.right = target.right
        target.right.left = self.head
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        target = self.tail.left
        self.tail.left = target.left
        target.left.right = self.tail
        return True

    def getFront(self) -> int:
        if self.len == 0:
            return -1
        return self.head.right.val

    def getRear(self) -> int:
        if self.len == 0:
            return -1
        return self.tail.left.val

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k


myCircularDeque = MyCircularDeque(3)
print(myCircularDeque.insertLast(1))
print(myCircularDeque.insertLast(2))
print(myCircularDeque.insertFront(3))
print(myCircularDeque.insertFront(4))
print(myCircularDeque.getRear())
print(myCircularDeque.isFull())
print(myCircularDeque.deleteLast())
print(myCircularDeque.insertFront(4))
print(myCircularDeque.getFront())
