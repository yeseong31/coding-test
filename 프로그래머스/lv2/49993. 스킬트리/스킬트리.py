import re


def solution(skill: str, skill_trees: list) -> int:
    answer = 0
    
    for skill_tree in skill_trees:
        target = re.sub(f'[^{skill}]', '', skill_tree)
        if skill.startswith(target):
            answer += 1
    
    return answer