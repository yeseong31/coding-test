def solution(n: int, works: list):
    works.sort(reverse=True)
    length = len(works)

    while n > 0:
        for i in range(length):
            works[i] -= 1
            n -= 1
            
            if n == 0:
                return sum(x ** 2 for x in works if x > 0)
            
            if i < length - 1 and works[i] >= works[i + 1]:
                break
