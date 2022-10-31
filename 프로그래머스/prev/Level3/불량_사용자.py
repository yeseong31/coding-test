import itertools


def solution(user_id, banned_id):
    def check(uid, bid):
        if len(uid) != len(bid):
            return False
        for u, b in zip(uid, bid):
            if b != '*' and u != b:
                return False
        return True

    answer = []

    for perm in itertools.permutations(user_id, len(banned_id)):
        cnt = 0
        for uid, bid in zip(perm, banned_id):
            if check(uid, bid):
                cnt += 1
        target = set(perm)
        if cnt == len(banned_id) and target not in answer:
            answer.append(target)

    return len(answer)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))

