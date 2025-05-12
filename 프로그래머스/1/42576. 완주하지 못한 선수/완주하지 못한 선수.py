from itertools import zip_longest


def solution(participant, completion):
    for p, c in zip_longest(sorted(participant), sorted(completion)):
        if p != c:
            return p
    