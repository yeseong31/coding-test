def solution(a, b, n):
    answer = 0
    while n >= a:
        div, mod = divmod(n, a)
        div *= b
        answer += div
        n = div + mod
    return answer