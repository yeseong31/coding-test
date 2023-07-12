def solution(name, yearning, photo):
    answer = []
    scores = {name: score for name, score in zip(name, yearning)}
    for target in photo:
        answer.append(sum(scores[t] for t in target if t in scores))
    return answer