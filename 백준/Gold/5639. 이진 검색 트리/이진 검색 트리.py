import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline


def dfs(node, end):
    if node > end:
        return
    mid = end + 1
    for i in range(node + 1, end + 1):
        if tree[node] < tree[i]:
            mid = i
            break
    # pre-order
    dfs(node + 1, mid - 1)
    dfs(mid, end)
    print(tree[node])


tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break
dfs(0, len(tree) - 1)
