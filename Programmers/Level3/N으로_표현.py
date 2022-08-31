def solution(N, number):
    # 결괏값
    answer = -1
    # d[i]: i-1번째 구성 요소의 사칙 연산 결과 저장
    d = []

    # 숫자의 길이 i를 증가시키면서 확인
    for i in range(1, 10):
        # 연산식 저장
        check = set()
        # 연산할 숫자
        check.add(int(str(N) * i))
        # i-1번째 구성 요소에 대해 사칙 연산 결과 저장
        for j in range(i - 1):
            for x in d[j]:
                for y in d[-j - 1]:
                    check.add(x + y)
                    check.add(x - y)
                    check.add(x * y)
                    if y != 0:
                        check.add(x / y)
        # 결과 확인
        if number in check:
            return i
        # 연산 결과 저장
        d.append(check)

    return answer
