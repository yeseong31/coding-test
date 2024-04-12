def solution(s):
    answer = []
    word = dict()
    
    for i, c in enumerate(s):
        answer.append(i - word[c] if c in word else -1)
        word[c] = i
    
    return answer
