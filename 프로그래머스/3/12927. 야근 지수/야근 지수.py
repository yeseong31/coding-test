def solution(n: int, works: list):
    works.sort(reverse=True)

    while n > 0:
        for i, _ in enumerate(works):
            works[i] -= 1
            n -= 1
            
            if n == 0:
                return sum(x ** 2 for x in works if x > 0)
            if i < len(works) - 1 and works[i] >= works[i + 1]:
                break
                
    return 0
