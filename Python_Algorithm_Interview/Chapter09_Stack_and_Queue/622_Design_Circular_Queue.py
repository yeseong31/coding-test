# 원형 큐 디자인(259p)

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.front = self.rear = 0
        self.maxLen = k

    def enQueue(self, value: int) -> bool:
        # 큐가 꽉 찼으면 넣으면 안 됨
        if self.q[self.rear] is not None:
            return False
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.maxLen
        return True

    def deQueue(self) -> bool:
        # 큐에서 뺄 게 없으면
        if self.q[self.front] is None:
            return False
        self.q[self.front] = None
        self.front = (self.front + 1) % self.maxLen
        return True

    def Front(self) -> int:
        if self.q[self.front] is None:
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.q[self.rear - 1] is None:
            return -1
        return self.q[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.q[self.front] is None

    def isFull(self) -> bool:
        return self.front == self.rear and self.q[self.front] is not None
