def solution(n):
    answer = []
    hanoi(1, 2, 3, n, answer)
    return answer


def hanoi(start, mid, end, n, answer):
    if n == 1:
        answer.append([start, end])
        return 

    hanoi(start, end, mid, n - 1, answer)
    hanoi(start, mid, end, 1, answer)
    hanoi(mid, start, end, n - 1, answer)
