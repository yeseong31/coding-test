from collections import deque


def solution(n):
    answer = deque()

    while n:
        if n % 3 == 0:
            answer.appendleft('4')
            n //= 3
            n -= 1
        else:
            answer.appendleft(str(n % 3))
            n //= 3

    return ''.join(answer)
