import collections


def preorder(x):
    if x != '.':
        print(x, end='')
        preorder(graph[x][0])
        preorder(graph[x][1])


def inorder(x):
    if x != '.':
        inorder(graph[x][0])
        print(x, end='')
        inorder(graph[x][1])


def postorder(x):
    if x != '.':
        postorder(graph[x][0])
        postorder(graph[x][1])
        print(x, end='')


n = int(input())

graph = collections.defaultdict(list)
for _ in range(n):
    val, left, right = input().split()
    graph[val] = [left, right]

# 전위 순회
preorder('A')
print()
# 중위 순회
inorder('A')
print()
# 후위 순회
postorder('A')
print()
