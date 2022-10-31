def solution(n, works):
    works.sort(reverse=True)
    i = 0
    while True:
        works[i] -= 1
        n -= 1
        if n == 0:
            break
        if i == len(works) - 1 or works[i] >= works[i + 1]:
            i = 0
        else:
            i += 1
    return sum([x ** 2 for x in works if x >= 0])


works = [1, 1]
print(solution(3, works))


# 야근 피로도 = 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값

