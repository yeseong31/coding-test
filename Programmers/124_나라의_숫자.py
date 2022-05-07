def solution(n):
    answer = ''

    while n:
        # 3으로 나누어 떨어지는 경우
        if n % 3 == 0:
            answer += '4'
            n = n // 3 - 1
        else:
            answer += str(n % 3)
            n //= 3

    return answer[::-1]