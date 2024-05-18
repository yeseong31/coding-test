def solution(s):
    count_zero = 0
    repeat = 0
    
    while s != '1':
        target = s.replace('0', '')
        count_zero += len(s) - len(target)
        s = bin(len(target))[2:]
        repeat += 1
    
    return repeat, count_zero
