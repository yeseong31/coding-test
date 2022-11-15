def solution(n, s):
    if n > s:
        return [-1]
    
    # s를 n으로 나눈 값을 n번 반복, 남은 mod를 answer에 1씩 더해줌
    div, mod = divmod(s, n)
    answer = [div] * n
    
    while mod > 0:
        answer[n - 1] += 1
        n -= 1
        mod -= 1

    return answer