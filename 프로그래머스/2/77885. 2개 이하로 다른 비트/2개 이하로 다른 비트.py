def find_result(x):
    if x % 2 == 0:
        return x + 1

    target = f'0{bin(x)[2:]}'
    idx = target.rindex('0')
    result = f'{target[:idx]}10{target[idx+2:]}'
    
    return int(result, 2)


def solution(numbers):    
    return [find_result(n) for n in numbers]
