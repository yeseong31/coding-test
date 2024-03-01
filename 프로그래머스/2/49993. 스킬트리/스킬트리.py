from re import sub


def solution(skill, skill_trees):
    return sum(skill.startswith(sub(f'[^{skill}]', '', tree)) for tree in skill_trees)
