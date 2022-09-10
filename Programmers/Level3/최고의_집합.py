def solution(n, s):
    if n > s:
        return [-1]

    div, mod = divmod(s, n)
    answer = [div] * n

    for i in range(mod):
        answer[len(answer) - i - 1] += 1

    return answer


n, s = 2, 9
print(solution(n, s))

n, s = 2, 1
print(solution(n, s))

n, s = 3, 8
print(solution(n, s))
