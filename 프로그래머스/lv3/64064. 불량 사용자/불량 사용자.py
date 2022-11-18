from itertools import permutations


def solution(user_id, banned_id):
    def check_id(bid, uid):
        if len(bid) != len(uid):
            return False
        for b, u in zip(bid, uid):
            if b != '*' and b != u:
                return False
        return True

    answer = []    
    for perm in permutations(user_id, len(banned_id)):
        count = 0
        for bid, uid in zip(banned_id, perm):
            if check_id(bid, uid):
                count += 1
        check_id_set = set(perm)
        if count == len(banned_id) and check_id_set not in answer:
            answer.append(check_id_set)
    
    return len(answer)