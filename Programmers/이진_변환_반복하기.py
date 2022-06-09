import time


def solution(s):
    tries = sum_value = 0
    while s != '1':
        # x의 모든 0 제거
        cnt = s.count('0')
        sum_value += cnt

        # 2진수로 변환
        s = str(bin(len(s) - cnt))[2:]
        tries += 1

    return [tries, sum_value]


s = "1111111"
print(solution(s))
