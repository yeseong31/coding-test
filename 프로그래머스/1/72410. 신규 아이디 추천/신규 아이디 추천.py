import re


def solution(new_id):
    s = new_id.lower()
    s = re.sub('[^a-z0-9\_\-\.]', '', s)
    s = re.sub('[.]+', '.', s)
    s = s.strip('.')
    s = s if s else 'a'
    s = s[:15]
    s = s.strip('.')
    s = s if len(s) >= 3 else s + ''.join(s[-1] for _ in range(3 - len(s)))
    return s