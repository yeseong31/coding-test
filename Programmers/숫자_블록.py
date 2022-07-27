def solution(begin, end):
    def find(n):
        if n == 1:
            return 0
        for i in range(2, int(n ** 0.5) + 1):
            div, mod = divmod(n, i)
            if div > 10000000:
                continue
            if mod == 0:
                return div
        return 1

    answer = []
    for n in range(begin, end + 1):
        answer.append(find(n))
    return answer


print(solution(1, 30))
