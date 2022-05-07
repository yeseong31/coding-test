def solution(left, right):
    answer = 0

    for n in range(left, right + 1):
        # 제곱수의 약수의 개수는 홀수
        answer -= n if int(n ** 0.5) == n ** 0.5 else -n
    return answer