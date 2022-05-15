# 모든 조합 탐색

def letterCombinations(digits: str) -> list[str]:
    def dfs(idx, path):
        if len(path) == len(digits):
            res.append(path)
            return

        for i in range(idx, len(digits)):
            for j in dic[digits[idx]]:
                dfs(i + 1, path + j)

    if not digits:
        return []

    dic = {
        '2': 'abc', '3': 'def',
        '4': 'ghi', '5': 'jkl', '6': 'mno',
        '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    res = []
    dfs(0, '')
    return res
