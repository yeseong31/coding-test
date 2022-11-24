from itertools import permutations


def solution(ability):
    answer = 0
    n, m = len(ability), len(ability[0])
    for perm in permutations(range(n), m):
        answer = max(answer, sum([ability[i][j] for i, j in zip(perm, list(range(m)))]))
    return answer


ability = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]
print(solution(ability))

ability = [[20, 30], [30, 20], [20, 30]]
print(solution(ability))

