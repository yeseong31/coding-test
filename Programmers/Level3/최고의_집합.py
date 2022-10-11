def solution(n, s):
    if n > s:
        return [-1]
    div, mod = divmod(s, n)
    answer = [div] * n
    i = n - 1
    while mod != 0:
        answer[i] += 1
        i -= 1
        mod -= 1
    return answer


n, s = 2, 9
print(solution(n, s))

n, s = 2, 1
print(solution(n, s))

n, s = 2, 8
print(solution(n, s))
