class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_VALUE = 0x7FFFFFFF

        # 덧셈 및 자릿수 처리
        while b != 0:
            # a: carry 값을 고려하지 않는 a와 b의 합 저장
            # b: 자릿수를 올려가며 carry 값 저장
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        # 음수 처리
        if MAX_VALUE < a:
            a = ~(a ^ MASK)
        return a


# 아래는 논리 회로(전가산기)를 직접 구현하는 풀이
class Solution2:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_VALUE = 0x7FFFFFFF

        BIT = 32
        res = []
        c = 0

        # 전처리 및 마스킹 작업
        a = bin(a & MASK)[2:].zfill(BIT)
        b = bin(b & MASK)[2:].zfill(BIT)

        for i in range(BIT - 1, -1, -1):
            p, q = int(a[i]), int(b[i])
            # 전가산기
            # https://ko.wikipedia.org/wiki/%EA%B0%80%EC%82%B0%EA%B8%B0
            g1 = p & q
            g2 = p ^ q
            g3 = g2 & c
            s = g2 ^ c
            c = g1 | g3
            res.append(str(s))
        if c == 1:
            res.append('1')

        # 자릿수 오버플로 처리
        res = int(''.join(res[::-1]), 2) & MASK
        # 양수 최댓값을 넘어서면 '음수'
        if MAX_VALUE < res:
            res = ~(res ^ MASK)
        return res
