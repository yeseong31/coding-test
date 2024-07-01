def solution(X, Y):
    answer = [c for c in '9876543210' for _ in range(min(X.count(c), Y.count(c)))]
    if not answer:
        return '-1'
    if answer.count('0') == len(answer):
        return '0'
    return ''.join(answer)
