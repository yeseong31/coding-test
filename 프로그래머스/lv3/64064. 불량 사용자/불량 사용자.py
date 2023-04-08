from re import fullmatch


def dfs(idx, visit, answer, user_id, ban_patterns):
    if idx == len(ban_patterns):
        answer.add(visit)
        return
    # 다음 제재 아이디와 다음 방문 상태를 점검하여 규칙이 서로 일치하는지 확인
    for i in range(len(user_id)):
        # 방문 여부 확인: and 연산
        if visit & (1 << i) > 0 or not fullmatch(ban_patterns[idx], user_id[i]):
            continue
        # 다음 위치 생성: or 연산
        dfs(idx + 1, visit | (1 << i), answer, user_id, ban_patterns)


def solution(user_id, banned_id):
    answer = set()
    ban_patterns = [x.replace('*', '.') for x in banned_id]
    dfs(0, 0, answer, user_id, ban_patterns)
    return len(answer)
