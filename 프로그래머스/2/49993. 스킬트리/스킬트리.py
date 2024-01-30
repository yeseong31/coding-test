from re import sub


def solution(skill, skill_trees):
    return sum(skill.startswith(sub(f'[^{skill}]', '', skill_tree)) for skill_tree in skill_trees)
