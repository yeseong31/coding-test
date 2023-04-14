def dfs(start, end, tree):
    if start >= end:
        return tree[start]
    mid = (start + end) // 2
    left = dfs(start, mid - 1, tree)
    if not left or (tree[mid] == '0' and left == '1'):
        return False
    right = dfs(mid + 1, end, tree)
    if not right or (tree[mid] == '0' and right == '1'):
        return False
    if left == right == tree[mid] == '0':
        return '0'
    return '1'
        

def solution(numbers):
    answer = []
    for n in numbers:
        s = bin(n)[2:]
        i = 1
        while 2 ** i - 1 < len(s):
            i += 1
        tree = s.zfill(2 ** i - 1)
        answer.append(1 if dfs(0, len(tree) - 1, tree) else 0)
    return answer
