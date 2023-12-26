def solution(files):
    answer = []
    
    for file in files:
        head, number, tail = '', '', ''
        flag = True
        
        for i, v in enumerate(file):
            if flag and (v.isalpha() or v in ('-', ' ', ',')):
                head += v
                continue
            if v.isdigit():
                flag = False
                number += v
                continue
            
            tail += file[i:]
            break
        
        answer.append([head, number, tail])

    return [''.join(v) for v in sorted(answer, key=lambda x: (x[0].lower(), int(x[1])))]
