"""
연산자 끼워 넣기 (349p)
"""


n = int(input())
# 피연산자
operands = list(map(int, input().split()))
# 연산자
add, sub, mul, div = map(int, input().split())

# 최솟값, 최댓값
min_value = int(1e9)
max_value = -int(1e9)


def dfs(cnt, num):
    global min_value, max_value, add, sub, mul, div

    # 주어진 연산자를 모두 사용한 경우에만 최솟값, 최댓값 계산
    if cnt == n:
        max_value = max(max_value, num)
        min_value = min(min_value, num)
    # 그렇지 않으면 연산자를 추가하는 과정 수행
    else:
        # 더하기
        if add > 0:
            add -= 1
            dfs(cnt + 1, num + operands[cnt])
            add += 1
        # 빼기
        if sub > 0:
            sub -= 1
            dfs(cnt + 1, num - operands[cnt])
            sub += 1
        # 곱하기
        if mul > 0:
            mul -= 1
            dfs(cnt + 1, num * operands[cnt])
            mul += 1
        # 나누기
        if div > 0:
            div -= 1
            dfs(cnt + 1, int(num / operands[cnt]))
            div += 1


# 연산 횟수 및 첫 피연산자를 dfs로 전달
dfs(1, operands[0])
print(max_value)
print(min_value)
