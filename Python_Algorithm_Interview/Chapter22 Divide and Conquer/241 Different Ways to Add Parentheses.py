# 숫자와 연산자를 입력받아 가능한 모든 조합의 결과를 출력하라.
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # 숫자만 있다면 그대로 반환
        if expression.isdigit():
            return [int(expression)]

        answer = []
        for i, v in enumerate(expression):
            # 연산자를 기준으로 식 분할
            if v in '+-*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                # 계산 값을 결과 리스트에 추가
                answer.extend([eval(str(l) + v + str(r)) for r in right for l in left])
        return answer


solution = Solution()

expression = "2-1-1"
print(solution.diffWaysToCompute(expression))

expression = "2*3-4*5"
print(solution.diffWaysToCompute(expression))
