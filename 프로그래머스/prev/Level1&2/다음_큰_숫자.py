def solution(n):
    target = bin(n)[2:]
    cnt = target.count('1')
    for nx in range(n + 1, 1000001):
        if bin(nx)[2:].count('1') == cnt:
            return nx
    return -1


print(solution(78))

# 현재 숫자 cur, 다음 숫자 nx
# cur과 nx의 1의 개수는 같음
# nx는 후보가 될 수 있는 숫자들 중에서 가장 작음
