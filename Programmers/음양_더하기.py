def solution(absolutes, signs):
    answer = 0

    for n, sign in zip(absolutes, signs):
        answer += n if sign else -n

    return answer