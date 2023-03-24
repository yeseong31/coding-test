def solution(ability):
    def dfs(depth, selected, dp):
        # m명의 학생을 모두 확인했다면 종료
        if depth == len(ability[0]):
            return 0
        # 이미 선택한 학생을 다시 선택하는 경우를 제외하고 모두 선택할 때까지 재귀 반복
        if not dp[selected]:
            for i in range(len(ability)):
                # 현재 위치 & 선택한 학생과 다음에 검사할 학생을 and 연산하여 학생 선택 여부 검사
                if selected & (1 << i):
                    continue
                current = ability[i][depth]
                # 현재 위치 & 선택한 학생과 다음에 검사할 학생을 or 연산하여 다음 학생 선택
                select = dfs(depth + 1, selected | (1 << i), dp)
                dp[selected] = max(current + select, dp[selected])
        return dp[selected]

    # 비트마스킹을 사용하여 학생 수, 종목 수에 대한 전체 경우의 수 관리
    # 비트마스킹 사용 시 2진법의 결과를 감안한 크기로 생성해야 함 -> 종목 수를 왼쪽으로 비트 시프트
    dp = [0] * (1 << len(ability))
    return dfs(0, 0, dp)
