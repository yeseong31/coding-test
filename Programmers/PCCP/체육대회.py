import itertools


def solution(ability):
    # 결과: 선발된 대표들의 해당 종목에 대한 능력치 합의 최댓값
    answer = 0
    # 종목의 수
    e = len(ability[0])
    # 학생의 수
    s = len(ability)
    # 학생 선택 및 능력치 계산
    for comb in list(itertools.permutations(range(s), e)):
        answer = max(answer, sum([ability[c][i] for i, c in enumerate(comb)]))
    return answer


ability = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]
print(solution(ability))

ability = [[20, 30], [30, 20], [20, 30]]
print(solution(ability))

