import re


def solution(new_id):
    answer = re.sub(r'[^a-z0-9._-]', '', new_id.lower())
    answer = re.sub('\.\.+', '.', answer)
    answer = answer.strip('.')
    
    if answer == '':
        answer = 'a'
        
    answer = answer[:15].strip('.')
    
    while len(answer) < 3:
        answer += answer[-1]
    
    return answer
