from collections import deque


def solution(N, number):
    dp = [set() for _ in range(9)]

    for i in range(1, 9):
        target = dp[i]
        target.add(int(str(N) * i))
        
        for j in range(1, i):
            for k in dp[j]:
                for l in dp[i - j]:
                    if k < number:
                        target.add(k + l)
                        target.add(k * l)
                    if k > 0:
                        target.add(k - l)
                    if k != 0 and l != 0:
                        target.add(k // l)
        
        if number in target:
            return i
        
    return -1