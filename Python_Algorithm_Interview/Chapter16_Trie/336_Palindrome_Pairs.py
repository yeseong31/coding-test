"""
팰린드롬 페어(466p)
- 단어 리스트에서 words[i] + words[j]가 팰린드롬이 되는 모든 인덱스 조합 (i, j)를 구하라
"""
import collections
from typing import List


class Node:
    def __init__(self):
        self.word_id = -1
        self.children = collections.defaultdict(Node)
        self.palindrome_word_ids = []  # 팰린드롬 형태를 가지는 단어의 인덱스들


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, idx, word):
        node = self.root

        # 입력값을 뒤집어서 트라이 구성 (팰린드롬 판별을 위해)
        for i, c in enumerate(reversed(word)):
            # 단어 자체가 팰린드롬 형태를 가진다면
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_ids.append(idx)

            node = node.children[c]
            node.val = c

        # 단어가 끝나는 지점에는 단어 인덱스를 부여
        node.word_id = idx

    # 단어를 뒤집어서
    def search(self, idx, word):
        result = []
        node = self.root

        while word:
            # 탐색 중간에 word_id가 있고 나머지 문자가 팰린드롬인 경우
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([idx, node.word_id])
            if not word[0] in node.children:
                return result

            node = node.children[word[0]]
            word = word[1:]

        # 끝까지 탐색했을 때 word_id가 있는 경우
        if node.word_id >= 0 and node.word_id != idx:
            result.append([idx, node.word_id])

        # 끝까지 탐색했을 때 palindrome_word_ids가 있는 경우
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([idx, palindrome_word_id])

        return result

    @staticmethod
    def is_palindrome(s):
        return s[::] == s[::-1]


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i, w in enumerate(words):
            trie.insert(i, w)

        result = []
        for i, w in enumerate(words):
            result.extend(trie.search(i, w))
        return result


# 간단하지만 LeetCode에서는 '타임아웃'으로 테스트 케이스를 통과하지 못 함
# class Solution:
#     def palindromePairs(self, words: List[str]) -> List[List[int]]:
#         def is_palindrome(s) -> bool:
#             return s == s[::-1]
#
#         answer = []
#
#         for i, word1 in enumerate(words):
#             for j, word2 in enumerate(words):
#                 if i == j:
#                     continue
#                 if is_palindrome(word1 + word2):
#                     answer.append([i, j])
#
#         return answer


solution = Solution().palindromePairs
words = ["abcd","dcba","lls","s","sssll"]
print(solution(words))
