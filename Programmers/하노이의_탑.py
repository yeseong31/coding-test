def solution(n):
    def hanoi(i, a, b, c):
        if i == 1:
            answer.append([a, c])
            return
        hanoi(i - 1, a, c, b)
        answer.append([a, c])
        hanoi(i - 1, b, a, c)

    answer = []
    hanoi(n, 1, 2, 3)
    return answer


print(solution(4))
