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
            if t not in btn:
                check = True
                break
            
            result += btn[t]
            
        answer.append(result if not check else -1)
    
    return answer
