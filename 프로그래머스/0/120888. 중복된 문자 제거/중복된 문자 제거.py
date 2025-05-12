def solution(my_string):
    answer = []
    checked = set()
    
    for c in my_string:
        if c not in checked:
            checked.add(c)
            answer.append(c)
    
    return ''.join(answer)