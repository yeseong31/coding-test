# 매번 각각 1계단 또는 2계단씩 오를 수 있다면 정상에 도달하기 위한 방법은 몇 가지 경로가 되는가


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        d = [0] * (n + 1)
        d[1] = 1
        d[2] = 2
        for i in range(3, n + 1):
            d[i] = d[i - 1] + d[i - 2]
        return d[n]


solution = Solution()

n = 4
print(solution.climbStairs(n))
