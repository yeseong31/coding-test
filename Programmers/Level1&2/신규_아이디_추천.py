import re


def solution(new_id):
    answer = re.sub('[^a-z\d\w\.\-\_]', '', new_id.lower())
    answer = re.sub('\.\.+', '..', answer)
    answer = re.sub('\.$', '', answer.lstrip('.'))
    if len(answer) == 0:
        answer = 'a'
    answer = re.sub('\.$', '', answer[:15])
    for _ in range(3 - len(answer)):
        answer += answer[-1]
    return answer
