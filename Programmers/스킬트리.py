import re


def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        check = True
        for i, r in enumerate(re.sub(f'[^{skill}]', '', tree)):
            if skill[i] != r:
                check = False
                break
        if check:
            answer += 1


skill = 'CBD'
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))
