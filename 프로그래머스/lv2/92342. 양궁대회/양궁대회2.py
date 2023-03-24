def compare(cur, prev):
    for i in range(10, 0, -1):
        if cur[i] > prev[i]:
            return True
        elif cur[i] < prev[i]:
            return False


def calc(ryan, apeach):
    result = 0
    for i in range(11):
        if ryan[i] > apeach[i]:
            result += 10 - i
        elif ryan[i] < apeach[i]:
            result -= 10 - i
    return result


# 어피치 점수(info), i번째 화살, 최고 기록, 라이언 화살 위치(list), 사용한 화살 수
def dfs(apeach, i, case, choose, n):
    if n < 0 or i == 11:
        return
    if i == 10 and n >= 0:
        # 라이언 점수표
        ryan = [*choose, n]
        # 어피치와 라이언의 점수 비교
        total = calc(ryan, apeach)
        # 총점이 더 높거나 낮은 과녁을 더 많이 맞힌 경우 case 갱신
        if total > case[0]:
            case[0] = total
            case[1] = ryan
        elif total == case[0] and compare(ryan, case[1]):
            case[1] = ryan

    # 높은 점수 과녁에 한 발 더 쏜 경우와 아예 쏘지 않고 넘긴 경우를 확인
    dfs(apeach, i + 1, case, [*choose, apeach[i] + 1], n - (apeach[i] + 1))
    dfs(apeach, i + 1, case, [*choose, 0], n)


def solution(n, info):
    answer = [0, [0] * 11]
    dfs(info, 0, answer, [], n)
    return [-1] if not answer[0] else answer[1]
