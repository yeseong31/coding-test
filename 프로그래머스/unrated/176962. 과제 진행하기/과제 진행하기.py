def solution(plans):
    answer, stack = [], []
    plans = sorted([(int(s[:2]) * 60 + int(s[3:]), int(p), n) for n, s, p in plans])
    
    for i, (start, playing, name) in enumerate(plans):
        if i == len(plans) - 1:
            answer.append(name)
            continue
        
        n_start = plans[i + 1][0]
        if n_start < start + playing:
            stack.append((start, start + playing - n_start, name))
            continue
        
        answer.append(name)
        tmp = n_start - (start + playing)
        
        while stack and tmp != 0:
            p_start, p_playing, p_name = stack.pop()
            if tmp < p_playing:
                stack.append((p_start, p_playing - tmp, p_name))
                tmp = 0
                continue
            tmp -= p_playing
            answer.append(p_name)
    
    while stack:
        answer.append(stack.pop()[2])
    return answer
        