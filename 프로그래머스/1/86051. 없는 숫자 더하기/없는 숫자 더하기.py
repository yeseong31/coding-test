def solution(numbers):
    target = [n in numbers for n in range(10)]
    return sum(index for index, value in enumerate(target) if not value)
