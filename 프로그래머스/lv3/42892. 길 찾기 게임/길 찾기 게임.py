import sys
sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, i, x):
        self.i = i
        self.x = x
        self.left = None
        self.right = None
        

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, i, x):
        self.root = self._insert(self.root, i, x)
        return self.root is not None
    
    def _insert(self, node, i, x):
        if node is None:
            return Node(i, x)
        if x < node.x:
            node.left = self._insert(node.left, i, x)
        else:
            node.right = self._insert(node.right, i, x)
        return node
    
    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, node, result=None):
        if result is None:
            result = []
        if node:
            result.append(node.i)
            self._preorder(node.left, result)
            self._preorder(node.right, result)
        return result
    
    def postorder(self):
        return self._postorder(self.root)
    
    def _postorder(self, node, result=None):
        if result is None:
            result = []
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.i)
        return result


def solution(nodeinfo):
    tree = Tree()
    for x, _, i in sorted([(x, y, i) for i, (x, y) in enumerate(nodeinfo, 1)], key=lambda k: (-k[1], k[0])):
        tree.insert(i, x)
    return tree.preorder(), tree.postorder()
