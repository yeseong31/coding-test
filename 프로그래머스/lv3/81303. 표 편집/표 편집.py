class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.rm = False


def solution(n, k, cmd):
    answer = ''

    removes = []
    table = [Node(i - 1, i + 1) for i in range(n)]
    table[0].left = table[-1].right = None

    for target in cmd:
        if target[0] == 'C':
            removes.append(k)
            table[k].rm = True
            left, right = table[k].left, table[k].right
            if left is not None:
                table[left].right = right
                k = left
            if right is not None:
                table[right].left = left
                k = right

        elif target[0] == 'Z':
            r = removes.pop()
            table[r].rm = False
            left, right = table[r].left, table[r].right
            if left is not None:
                table[left].right = r
            if right is not None:
                table[right].left = r

        elif target[0] == 'U':
            x = int(target.split()[1])
            for _ in range(x):
                k = table[k].left

        elif target[0] == 'D':
            x = int(target.split()[1])
            for _ in range(x):
                k = table[k].right

    for node in table:
        answer += 'X' if node.rm else 'O'
    return answer