def solution(n, left, right):
    answer = []

    for v in range(left, right + 1):
        j = v % n
        i = v // n
        answer.append(max(i + 1, j + 1))

    return answer


n = 4
left, right = 7, 14
print(solution(n, left, right))

'''
def solution(n, left, right):
    return [max(v // n + 1, v % n + 1) for v in range(left, right + 1)]
'''
