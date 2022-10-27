import re
from collections import defaultdict


def solution(forms: list[list[str]]) -> list[str]:
    def check_exception(email, nickname):
        if len(email) < 11 or len(email) >= 20 or email.split('@')[1] != 'email.com':
            return True
        if len(nickname) < 1 or len(nickname) >= 20:
            return True
        if len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', nickname)) <= 0:
            return True
        return False

    answer = []
    dic = defaultdict(list)
    for email, nickname in forms:
        if check_exception(email, nickname):
            continue
        for i in range(len(nickname) - 1):
            dic[nickname[i:i + 2]].append(email)

    for target in dic:
        if len(dic[target]) >= 2:
            answer.extend(dic[target])

    return sorted(set(answer))


forms = [["jm@email.com", "제이엠"],
         ["jason@email.com", "제이슨"],
         ["woniee@email.com", "워니"],
         ["mj@email.com", "엠제이"],
         ["nowm@email.com", "이제엠"]]
print(solution(forms))
