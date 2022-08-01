def solution(numbers):
    target = [False] * 10
    for n in numbers:
        target[n] = True

    sum_value = 0
    for i, v in enumerate(target):
        if not v:
            sum_value += i

    return sum_value