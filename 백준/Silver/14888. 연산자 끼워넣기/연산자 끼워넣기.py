def dfs(cnt, value):
    global max_val, min_val, add, sub, mul, div

    # 연산 횟수가 정확히 n번이라면
    if cnt == n:
        max_val = max(max_val, value)
        min_val = min(min_val, value)
    # 그렇지 않다면 연산을 이어서 수행
    else:
        if add > 0:
            add -= 1
            dfs(cnt + 1, value + operands[cnt])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(cnt + 1, value - operands[cnt])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(cnt + 1, value * operands[cnt])
            mul += 1
        if div > 0:
            div -= 1
            dfs(cnt + 1, int(value / operands[cnt]))
            div += 1


# 숫자의 수
n = int(input())
# 피연산자
operands = list(map(int, input().split()))
# 연산자들
add, sub, mul, div = map(int, input().split())

# 최댓값, 최솟값 계산
max_val, min_val = -int(1e9), int(1e9)

# 연산 횟수, 연산 결과 전달
dfs(1, operands[0])

# 결과 출력
print(max_val)
print(min_val)