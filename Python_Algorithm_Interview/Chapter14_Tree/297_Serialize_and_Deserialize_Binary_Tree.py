# 이진 트리 직렬화 & 역직렬화(406p)
# 이진 트리를 배열로 직렬화하고, 반대로 역직렬화하는 기능을 구현하라.
# 즉 다음과 같은 트리는 [1, 2, 3, null, null, 4, 5]의 형태로 직렬화할 수 있다.
#           1
#          / \
#         2   3
#            / \
#           4   5


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
