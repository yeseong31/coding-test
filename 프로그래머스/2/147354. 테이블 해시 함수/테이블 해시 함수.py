def solution(data, col, row_begin, row_end):
    answer = -1
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    
    for row in range(row_begin, row_end + 1):    
        row_sum = sum(x % row for x in data[row - 1])
        target = int(bin(row_sum), 2)
        if answer == -1:
            answer = target
        else:
            answer ^= target
            
    return answer
