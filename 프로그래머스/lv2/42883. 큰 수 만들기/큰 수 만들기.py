def solution(number, k):
    answer = []
    for i, n in enumerate(number):
        while k > 0 and answer and answer[-1] < n:
            answer.pop()
            k -= 1
        answer.append(n)
    while k > 0:
        answer.pop()
        k -= 1
    return ''.join(answer)