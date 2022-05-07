def solution(numbers):
    return str(int(''.join(sorted([str(n) for n in numbers], key=lambda x: x * 3, reverse=True))))