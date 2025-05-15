import sys
sys.setrecursionlimit(10_000)

class Node:
    def __init__(self, x, y, k):
        self.x = x
        self.y = y
        self.k = k
        self.left = None
        self.right = None
        
        
class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, x, y, k):
        self.root = self._insert(self.root, x, y, k)
        return self.root is not None
    
    def _insert(self, node, x, y, k):
        if node is None:
            return Node(x, y, k)
        if x < node.x:
            node.left = self._insert(node.left, x, y, k)
        else:
            node.right = self._insert(node.right, x, y, k)
        return node
    
    def preorder(self):
        return self._preorder(self.root, [])
    
    def _preorder(self, node, result):
        if node:
            result.append(node.k)
            self._preorder(node.left, result)
            self._preorder(node.right, result)
        return result
    
    def postorder(self):
        return self._postorder(self.root, [])
    
    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.k)
        return result


def solution(nodeinfo):
    tree = Tree()
    
    nodes = [(x, y, i) for i, (x, y) in enumerate(nodeinfo, 1)]
    nodes.sort(key=lambda n: (-n[1], n[0]))
    
    for x, y, i in nodes:
        tree.insert(x, y, i)
    
    return tree.preorder(), tree.postorder()
