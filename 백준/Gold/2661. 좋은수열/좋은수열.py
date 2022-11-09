n = int(input())
answer = ''
target = ['1', '2', '3']


def dfs(p, stack):
    # 현재 수열의 자릿수의 절반만큼 중복 확인
    for i in range(1, p // 2 + 1):
        left, mid = -2 * i, -i
        if stack[left:mid] == stack[mid:]:
            return False
    if p == n:
        print(''.join(stack))
        return True
    for x in target:
        stack.append(x)
        if dfs(p + 1, stack):
            return True
        stack.pop()
    

dfs(0, [])