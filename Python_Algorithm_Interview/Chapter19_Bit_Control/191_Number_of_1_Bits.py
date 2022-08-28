# 부호없는 정수형을 입력받아 1비트의 개수를 출력하라

# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         return bin(n).count('1')


class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            n &= n - 1
            cnt += 1
        return cnt
