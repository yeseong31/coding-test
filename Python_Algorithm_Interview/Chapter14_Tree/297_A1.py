# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        q = collections.deque([root])
        result = ['#']

        # 트리 BFS 직렬화
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                result.append(str(node.val))
            else:
                result.append('#')

        return ' '.join(result)

    def deserialize(self, data: str) -> TreeNode:
        # 예외 처리
        if data == '# #':
            return None

        # 공백 단위로 문자열을 끊어서 nodes 리스트 변수로 만듦
        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        q = collections.deque([root])

        # 빠른 런너처럼 자식 노드 결과를 먼저 확인한 수 큐에 삽입
        idx = 2
        while q:
            node = q.popleft()
            if nodes[idx] is not '#':
                node.left = TreeNode(int(nodes[idx]))
                q.append(node.left)
            idx += 1
            if nodes[idx] is not '#':
                node.right = TreeNode(int(nodes[idx]))
                q.append(node.right)
            idx += 1

        # '#'의 경우 큐에 삽입하지 않고, 아무런 처리를 해주지 않음
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
