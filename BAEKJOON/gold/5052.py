# 전화번호 목록
import sys


# 풀이 1 (30840KB, 220ms)
for _ in range(int(input())):
    n = int(input())
    phones = sorted([sys.stdin.readline().rstrip() for _ in range(n)])
    check = True
    for i in range(n - 1):
        if phones[i] == phones[i + 1][:len(phones[i])]:
            check = False
            break
    if not check:
        print('NO')
    else:
        print('YES')


# 풀이 2 (51316KB, 1336ms)
# import sys
#
#
# class Node:
#     def __init__(self):
#         self.word = False
#         self.child = {}
#
#
# class Trie:
#     def __init__(self):
#         self.root = Node()
#
#     def insert_and_check(self, word):
#         node = self.root
#         for w in word:
#             if w not in node.child:
#                 if node.word:
#                     return False
#                 node.child[w] = Node()
#             node = node.child[w]
#         node.word = True
#         return True
#
#
# for _ in range(int(input())):
#     n = int(input())
#     trie = Trie()
#     check = True
#     for phone in sorted([sys.stdin.readline().rstrip() for _ in range(n)]):
#         if not trie.insert_and_check(phone):
#             check = False
#             break
#     if check:
#         print('YES')
#     else:
#         print('NO')
