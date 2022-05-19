"""
208. 트라이 구현(461p)

트라이의 insert, search, startsWith 메소드를 구현하라.
"""


# 트라이를 저장할 노드는 별도의 클래스로 선언
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    # 트라이 구조에 word 삽입
    def insert(self, word: str) -> None:
        node = self.root
        # 루트부터 시작하여 Trie 만들기
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        # word에 대한 Tree 구축 완료 시 True로 전환
        node.word = True

    # word 탐색
    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.word

    # prefix로 시작하는 word가 존재하는지 확인
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
