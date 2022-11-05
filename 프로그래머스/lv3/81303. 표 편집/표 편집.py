class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.rm = False


class Table:
    def __init__(self, n: int, k: int):
        self.table = [Node(i - 1, i + 1) for i in range(n)]
        self.table[0].left = self.table[-1].right = None
        self.removes = []
        self.k = k

    def up(self, x):
        for _ in range(x):
            self.k = self.table[self.k].left

    def down(self, x):
        for _ in range(x):
            self.k = self.table[self.k].right

    def remove(self):
        self.removes.append(self.k)
        self.table[self.k].rm = True
        left, right = self.table[self.k].left, self.table[self.k].right
        if left is not None:
            self.table[left].right = right
            self.k = left
        if right is not None:
            self.table[right].left = left
            self.k = right

    def restore(self):
        r = self.removes.pop()
        self.table[r].rm = False
        left, right = self.table[r].left, self.table[r].right
        if left is not None:
            self.table[left].right = r
        if right is not None:
            self.table[right].left = r

    def get_table(self):
        return self.table


def solution(n, k, cmd):
    answer = ''
    table = Table(n, k)

    for target in cmd:
        if target[0] == 'C':
            table.remove()
        elif target[0] == 'Z':
            table.restore()
        elif target[0] == 'U':
            table.up(int(target.split()[1]))
        elif target[0] == 'D':
            table.down(int(target.split()[1]))

    for node in table.get_table():
        answer += 'X' if node.rm else 'O'
    return answer
