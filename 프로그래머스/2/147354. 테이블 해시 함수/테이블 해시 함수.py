def solution(data, col, row_begin, row_end):
    answer = -1
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    
    for i in range(row_begin, row_end + 1):    
        target = int(bin(sum(x % i for x in data[i - 1])), 2)
        
        if answer == -1:
            answer = target
        else:
            answer ^= target
            
    return answer
