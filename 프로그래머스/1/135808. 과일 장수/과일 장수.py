def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    for i, _ in enumerate(score):
        if i % m == 0 and i + m <= len(score):
            answer += min(score[i:i+m])
            
    return answer * m