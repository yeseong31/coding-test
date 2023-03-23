class Node:
    def __init__(self):
        self.count = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for w in word:
            node.count += 1
            if w not in node.children:
                node.children[w] = Node()
            node = node.children[w]

    def search(self, word):
        node = self.root
        for w in word:
            if w == '?':
                break
            if w in node.children:
                node = node.children[w]
            else:
                return 0
        return node.count


def solution(words, queries):
    answer = []
    tries = {}
    reverse_tries = {}

    for word in words:
        length = len(word)
        if length not in tries:
            tries[length] = Trie()
            reverse_tries[length] = Trie()
        tries[length].insert(word)
        reverse_tries[length].insert(word[::-1])

    for query in queries:
        if len(query) not in tries:
            answer.append(0)
            continue
        if query[0] == '?':
            trie = reverse_tries[len(query)]
            answer.append(trie.search(query[::-1]))
        else:
            trie = tries[len(query)]
            answer.append(trie.search(query))

    return answer
