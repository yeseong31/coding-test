# Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            target = int(str(x)[::-1])
        else:
            target = -1 * int(str(x*-1)[::-1])
        if target not in range(-2 ** 31, 2 ** 31 + 1):
            return 0
        return target
