# 입력값이 UTF-8 문자열이 맞는지 검증하라.
from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check(n: int) -> bool:
            # 첫 바이트를 제외하고 뒤따르는 n바이트는 모두 '10'으로 시작해야 함
            for i in range(start + 1, start + n + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True

        start = 0
        while start < len(data):
            first_byte = data[start]
            if (first_byte >> 3) == 0b11110 and check(3):
                start += 4
            elif (first_byte >> 4) == 0b1110 and check(2):
                start += 3
            elif (first_byte >> 5) == 0b110 and check(1):
                start += 2
            elif (first_byte >> 7) == 0:
                start += 1
            else:
                return False
        return True


solution = Solution()
data = [197, 130, 1]
print(solution.validUtf8(data))
