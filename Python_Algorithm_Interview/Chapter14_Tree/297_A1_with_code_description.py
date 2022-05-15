# 풀이 1 - 직렬화 & 역직렬화 구현

# 이진 트리 데이터 구조는 논리적인 구조이다.
# 이를 파일이나 디스크에 저장하기 위해서는 물리적인 형태로 바꿔줘야 하는데, 이를 직렬화(Serialize)라고 한다.
# 파이썬에는 pickle이라는 직렬화 모듈을 기본으로 제공한다.
# 파이썬 객체의 계층(Hierarchy) 구조를 바이트 스트림으로 변경하는 작업은 피클링(Pickling)이라고 한다.

# 이진 힙은 완전 이진 트리로서, 배열료 표현하기 매우 좋은 구조이다.
# 높이 순서대로 순회하면 모든 노드를 배열에 낭비 없이 배치할 수 있기 때문이다.
# 해당 노드의 인덱스를 알면 깊이가 얼마인지, 부모와 자식 노드가 배열 어디에 위치하는지 바로 알아낼 수 있다.
#   부모 노드:       i // 2
#   왼쪽 자식 노드:   2i
#   오른쪽 자식 노드: 2i + 1

# --------------------------------------------------------------------------------------------------
# [직렬화]
# 이 문제는 직렬화 알고리즘에 제약이 없지만, 가능하면 BFS 탐색 결과로 표현하여
# 배열만 봐도 트리의 형태를 직관적으로 떠올릴 수 있도록 이해하기 쉽게 구현하고자 한다.
#
#           A
#          / \          0 1 2 3 4 5 6 7         - 여기서는 Null 대신 #으로 표현
#         B   C           A B C # # D E         - 파이썬의 널인 None은 문자열 표현이 불가능하기 때문
#            / \
#           D   E       따라서, 직렬화 결과는... [#, A, B, C, #, #, D, E]

# BFS 탐색을 할 것이기 때문에 '#45 이진 트리 반전' 문제의 BFS 풀이의 구조를 변경하여 해결한다.

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

        return ''.join(result)

# --------------------------------------------------------------------------------------------------
# [역직렬화]
# 동일하게 큐를 이용하여 역직렬화를 진행한다.
    def deserialize(self, data: str) -> TreeNode:
        # 예외 처리
        if data == '# #':
            return None

        nodes = data.split()    # 공백 단위로 문자열을 끊어서 nodes 리스트 변수로 만듦

        root = TreeNode(int(nodes[1]))
        q = collections.deque([root])

        # 왼쪽/오른쪽 자식은 각각 별도의 인덱스를 부여받아 다음과 같이 nodes를 먼저 탐색해 나간다.
        # 마치 런너 기법에서 빠른 런너가 먼저 노드를 탐색해 나가는 것과 유사하다.
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

        # '#'의 경우 큐에 삽입하지 않고, 아무런 처리도 하지 않는다.
        return root
