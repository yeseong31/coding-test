def solution(n):
    cnt = 0
    while n >= 1:
        if n % 2 == 1:
            cnt += 1
            n -= 1
            continue
        n //= 2

    return cnt


print(solution(6))

