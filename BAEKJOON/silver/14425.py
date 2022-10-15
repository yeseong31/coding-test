# 문자열 집합
import sys
from collections import defaultdict

input = sys.stdin.readline


n, m = map(int, input().split())

str_set = {0, }
for _ in range(n):
    str_set.add(input())

cnt = 0
for _ in range(m):
    target = input()
    if target not in str_set:
        continue
    cnt += 1

print(cnt)


# 트라이 구현
# class Node:
#     def __init__(self):
#         self.word = False
#         self.children = defaultdict(Node)
#
#
# class Trie:
#     def __init__(self):
#         self.root = Node()
#
#     def insert(self, word: str) -> None:
#         node = self.root
#         for w in word:
#             if w not in node.children:
#                 node.children[w] = Node()
#             node = node.children[w]
#         node.word = True
#
#     def search(self, word: str) -> bool:
#         node = self.root
#         for w in word:
#             if w not in node.children:
#                 return False
#             node = node.children[w]
#         return node.word
#
#
# trie = Trie()
# n, m = map(int, input().split())
# for _ in range(n):
#     trie.insert(input())
#
# answer = 0
# for _ in range(m):
#     if trie.search(input()):
#         answer += 1
# print(answer)
