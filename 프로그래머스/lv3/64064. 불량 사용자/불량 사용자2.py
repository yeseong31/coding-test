from re import fullmatch
from itertools import permutations


def solution(user_id, banned_id):
    patterns = ' '.join(banned_id).replace('*', '.')
    answer = set(''.join(sorted(x)) for x in permutations(user_id, len(banned_id)) if fullmatch(patterns, ' '.join(x)))
    return len(answer)
