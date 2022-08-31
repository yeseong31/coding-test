import collections

import numpy as np


class Solution:
    d2 = collections.defaultdict(int)

    def fib(self, n: int) -> int:
        # 타뷸레이션 풀이 ------------------------------
        if n <= 1:
            return n

        d = [0] * (n + 1)
        d[1] = 1
        for i in range(2, n + 1):
            d[i] = d[i - 1] + d[i - 2]
        return d[n]

        # 메모이제이션 풀이 ------------------------------
        # if self.d2[n]:
        #     return self.d2[n]
        # self.d2[n] = self.fib2(n - 1) + self.fib2(n - 2)
        # return self.d2[n]

        # 두 변수만을 이용한 풀이 ------------------------------
        # x, y = 0, 1
        # for i in range(n):
        #     x, y = y, x + y
        # return y

        # 행렬을 이용한 풀이(LeetCode에서는 동작하지 않음) ------------------------------
        # m = np.matrix([[0, 1], [1, 1]])
        # vec = np.array([[0], [1]])
        # return np.matmul(m ** n, vec)[0]


solution = Solution()
print(solution.fib(10))
