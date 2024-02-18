from re import sub


def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        if skill.startswith(sub(f'[^{skill}]', '', tree)):
            answer += 1
    
    return answer
