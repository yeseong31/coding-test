def solution(word):
    def dfs(words: list, cur: str, length: int):
        if length >= 6:
            return
        if cur != '':
            words.append(cur)
        for x in 'AEIOU':
            dfs(words, cur + x, length + 1)
        
    data = []
    dfs(data, '', 0)
    return data.index(word) + 1