from heapq import heappush, heappop


class DoublePriorityQueue:
    def __init__(self):
        self.max_q = []
        self.min_q = []
        self.q_size = 0

    def add(self, value):
        heappush(self.max_q, -value)
        heappush(self.min_q, value)
        self.q_size += 1

    def remove_max_value(self):
        if self.q_size == 0:
            return

        self.q_size -= 1
        heappop(self.max_q)
        
        if self.q_size == 0:
            self.clear_queue()
        
    def remove_min_value(self):
        if self.q_size == 0:
            return

        self.q_size -= 1
        heappop(self.min_q)
        
        if self.q_size == 0:
            self.clear_queue()
            
    def receive_max_value(self):
        return -heappop(self.max_q) if self.q_size else 0
            
    def receive_min_value(self):
        return heappop(self.min_q) if self.q_size else 0
        
    def clear_queue(self):
        self.max_q.clear()
        self.min_q.clear()
        self.q_size = 0


def solution(operations):
    q = DoublePriorityQueue()

    for operation in operations:
        token, value = operation.split(' ')
        value = int(value)
        
        if token == 'I':
            q.add(value)
            continue
        
        if value < 0:
            q.remove_min_value()
        else:
            q.remove_max_value()

    return q.receive_max_value(), q.receive_min_value()
