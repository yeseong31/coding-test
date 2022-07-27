import math


def solution(n, k):
    answer = []
    num_list = list(range(1, n + 1))

    while n != 0:
        div, k = divmod(k, math.factorial(n - 1))
        if k == 0:
            answer.append(num_list.pop(div - 1))
        else:
            answer.append(num_list.pop(div))
        n -= 1

    return answer


print(solution(4, 13))
