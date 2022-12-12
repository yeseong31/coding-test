import sys
sys.setrecursionlimit(10 ** 4)


class Node:
    def __init__(self, x, v):
        self.left = None
        self.right = None
        self.x = x
        self.v = v

        
class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, x, v):
        self.root = self._insert(self.root, x, v)
        return self.root is not None

    def _insert(self, node, x, v):
        if node is None:
            return Node(x, v)
        if x < node.x:
            node.left = self._insert(node.left, x, v)
        else:
            node.right = self._insert(node.right, x, v)
        return node
    
    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, node, lst=[]):
        if lst is None:
            lst = []
        if node:
            lst.append(node.v)
            self._preorder(node.left, lst)
            self._preorder(node.right, lst)
        return lst
    
    def postorder(self):
        return self._postorder(self.root)
    
    def _postorder(self, node, lst=[]):
        if lst is None:
            lst = []
        if node:
            self._postorder(node.left, lst)
            self._postorder(node.right, lst)      
            lst.append(node.v)
        return lst    


def solution(nodeinfo):
    tree = Tree()
    for x, y, v in sorted([(x, y, i) for i, (x, y) in enumerate(nodeinfo, 1)], key=lambda w: (-w[1], w[0])):
        tree.insert(x, v)
    return tree.preorder(), tree.postorder()