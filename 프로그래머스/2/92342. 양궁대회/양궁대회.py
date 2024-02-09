from itertools import combinations_with_replacement


def get_ryan_board(scores):
    result = [0] * 11
    
    for score in scores:
        result[10 - score] += 1
    
    return result


def get_scores(apeach_board, ryan_board):
    apeach_score = ryan_score = 0
    
    for i, (a, b) in enumerate(zip(apeach_board, ryan_board)):
        score = 10 - i
        
        if a == b == 0:
            continue
        
        if a >= b:
            apeach_score += score
        else:
            ryan_score += score
    
    return apeach_score, ryan_score


def solution(n, info):
    answer = [-1]
    max_gap = -1
    
    for shoot in combinations_with_replacement(range(11), n):
        ryan_board = get_ryan_board(shoot)
        apeach_score, ryan_score = get_scores(info, ryan_board)
    
        if ryan_score <= apeach_score:
            continue
        
        if ryan_score - apeach_score > max_gap:
            max_gap = ryan_score - apeach_score
            answer = ryan_board
    
    return answer
