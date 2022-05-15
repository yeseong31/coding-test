# 전화 번호 문자 조합(338p)
# 2에서 9까지 숫자가 주어졌을 때 전화 번호로 조합 가능한 모든 문자를 출력하라.
def letterCombinations(digits: str) -> list[str]:
    def dfs(idx, result):
        # 끝까지 탐색하면 '백트래킹'
        if len(digits) == len(result):
            answer.append(result)
            return

        for i in range(idx, len(digits)):
            for j in alphabet[digits[i]]:
                dfs(i + 1, result + j)

    # 예외 처리
    if not digits:
        return []

    # 숫자-알파벳 매핑
    alphabet = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    answer = []
    dfs(0, '')
    return answer


digits = "23"
print(letterCombinations(digits))
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
