def solution(storey):
    answer = 0
    
    while storey != 0:
        div, mod = divmod(storey, 10)
        
        if mod == 0:
            storey = div
        elif mod >= 6 or mod == 5 and div % 10 >= 5:
            answer += 10 - mod
            storey += 10 - mod
        else:
            answer += mod
            storey -= mod
    
    return answer
