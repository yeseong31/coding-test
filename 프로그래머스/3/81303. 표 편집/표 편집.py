class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.removed = False
    
    
class Table:
    def __init__(self, n, k):
        self.table = [Node(i - 1, i + 1) for i in range(n)]
        self.table[0].left = None
        self.table[-1].right = None
        self.removed = []
        self.k = k
        
    def up(self, x):
        for _ in range(x):
            self.k = self.table[self.k].left
    
    def down(self, x):
        for _ in range(x):
            self.k = self.table[self.k].right
    
    def delete(self):
        self.removed.append(self.k)
        self.table[self.k].removed = True
        left, right = self.table[self.k].left, self.table[self.k].right
        
        if left is not None:
            self.table[left].right = right
            self.k = left
        if right is not None:
            self.table[right].left = left
            self.k = right
    
    def restore(self):
        node = self.removed.pop()
        self.table[node].removed = False
        left, right = self.table[node].left, self.table[node].right
        
        if left is not None:
            self.table[left].right = node
        if right is not None:
            self.table[right].left = node
        
    def get_result(self):
        answer = ''
        for node in self.table:
            answer += 'X' if node.removed else 'O'
        return answer


def solution(n, k, cmd):
    t = Table(n, k)
    for target in cmd:
        if target[0] == 'C':
            t.delete()
        elif target[0] == 'Z':
            t.restore()
        elif target[0] == 'U':
            t.up(int(target[2:]))
        elif target[0] == 'D':
            t.down(int(target[2:]))
    
    return t.get_result()
