def solution(n, works):
    works.sort(reverse=True)
    length = len(works)

    i = 0
    while True:
        # 작업량 1 처리
        works[i] -= 1
        n -= 1
        # 더 이상의 작업이 필요 없다면 그만
        if n == 0:
            break
        # 피로도가 가장 큰 작업들에 대한 처리가 끝났다면 다시 처음부터
        if i == length - 1 or works[i] >= works[i + 1]:
            i = 0
        # 다음 작업 확인
        else:
            i += 1

    answer = 0
    for work in works:
        if work > 0:
            answer += work ** 2
    return answer


works = [10, 1, 0]
print(solution(3, works))


# 야근 피로도 = 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값

