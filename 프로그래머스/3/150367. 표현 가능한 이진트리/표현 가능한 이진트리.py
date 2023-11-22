def dfs(start, end, tree):
    if start >= end:
        return tree[start]
    
    mid = (start + end) // 2
    
    left = dfs(start, mid - 1, tree)
    right = dfs(mid + 1, end, tree)
    
    if not left or (left == '1' and tree[mid] == '0'):
        return False

    if not right or (right == '1' and tree[mid] == '0'):
        return False
    
    if left == right == tree[mid] == '0':
        return '0'
    return '1'


def convert_to_full_binary_tree(binary_n):
    value = 1
    while 2 ** value - 1 < len(binary_n):
        value += 1
    
    return binary_n.zfill(2 ** value - 1)


def solution(numbers):
    answer = []
    
    for n in numbers:
        binary_n = bin(n)[2:]
        tree = convert_to_full_binary_tree(binary_n)
        
        answer.append(1 if dfs(0, len(tree) - 1, tree) else 0)
        
    return answer
