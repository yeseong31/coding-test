def solution(keymap, targets):
    answer = []
    btn = dict()
    
    for keys in keymap:
        for i, key in enumerate(keys, 1):
            if key not in btn or btn[key] > i:
                btn[key] = i
    
    for target in targets:
        result, check = 0, False
        
        for t in target:
            if t in btn:
                result += btn[t]
            else:
                check = True
                break
            
        if check:
            answer.append(-1)
        else:
            answer.append(result)
    
    return answer