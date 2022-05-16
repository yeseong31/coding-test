"""
가사 검색(370p)
"""
import collections


def solution(words, queries):
    # 트라이 노드
    class Node:
        def __init__(self):
            self.cnt = 0
            self.children = {}

    # 트라이 클래스
    class Trie:
        def __init__(self):
            self.root = Node()

        # word 삽입
        def insert(self, word):
            node = self.root
            for c in word:
                if c not in node.children:
                    node.children[c] = Node()
                node = node.children[c]
                node.cnt += 1

        # word 탐색
        def search(self, word):
            node = self.root
            for c in word:
                if c not in node.children:
                    return node.cnt
                node = node.children[c]
            return node.cnt

    answer = []

    # 트라이 구현
    trie = Trie()

    word_len_dic = collections.defaultdict(int)
    for word in words:
        length = len(word)
        word_len_dic[length] += 1
        trie.insert(str(length) + word)
        trie.insert(str(length) + word[::-1])

    dic = collections.defaultdict(int)
    for query in queries:
        # 중복 키워드 처리
        if query in answer:
            answer.append(dic[query])

        length = len(query)

        # 와일드카드 문자가 없으면
        if query.count('?') == 0:
            target = query
        # 와일드카드 문자로만 이루어졌다면
        elif query.count('?') == length:
            answer.append(word_len_dic[length])
            continue
        # 와일드카드 문자가 접두사라면
        elif query[0] == '?':
            query = query[::-1]
            target = query[:query.index('?')]
        # 와일드카드 문자가 접미사라면
        else:
            target = query[:query.index('?')]

        dic[target] = trie.search(str(len(query)) + target)
        answer.append(dic[target])

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["???rf"]
print(solution(words, queries))
