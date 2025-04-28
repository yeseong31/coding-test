def solution(s):
    seq = 0
    total_zero_count = 0
    
    while s != '1':
        zero_count = s.count('0')
        total_zero_count += zero_count
        
        s = bin(len(s) - zero_count)[2:]
        seq += 1
        
    return seq, total_zero_count