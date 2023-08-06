import sys
sys.setrecursionlimit(10000)


class Node:
    def __init__(self, x, y, v):
        self.left = None
        self.right = None
        self.x = x
        self.y = y
        self.v = v


class Tree:
    def __init__(self):
        self.root = None
    
    # 노드 추가
    def insert(self, x, y, v):
        self.root = self._insert(self.root, x, y, v)
        return self.root is not None
    
    def _insert(self, node, x, y, v):
        if node is None:
            return Node(x, y, v)
        if x < node.x:
            node.left = self._insert(node.left, x, y, v)
        else:
            node.right = self._insert(node.right, x, y, v)
        return node
    
    # 전위 순회
    def preorder(self):
        return self._preorder(self.root, [])
    
    def _preorder(self, node, result):
        if node:
            result.append(node.v)
            self._preorder(node.left, result)
            self._preorder(node.right, result)
        return result
    
    # 후위 순회
    def postorder(self):
        return self._postorder(self.root, [])
    
    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.v)
        return result


def solution(nodeinfo):
    nodeinfo = [(x, y, i) for i, (x, y) in enumerate(nodeinfo, 1)]
    nodeinfo.sort(key=lambda k: (-k[1], k[0]))
    
    tree = Tree()
    for x, y, i in nodeinfo:
        tree.insert(x, y, i)
    
    return tree.preorder(), tree.postorder()