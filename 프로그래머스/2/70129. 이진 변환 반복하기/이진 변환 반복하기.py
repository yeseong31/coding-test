def solution(s):
    countZero = 0
    repeat = 0
    
    while s != '1':
        target = s.replace('0', '')
        countZero += len(s) - len(target)
        s = bin(len(target))[2:]
        repeat += 1
    
    return repeat, countZero
