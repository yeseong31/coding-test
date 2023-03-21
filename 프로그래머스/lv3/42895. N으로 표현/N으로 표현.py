def solution(N, number):
    answer = 0
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        v = dp[i]
        v.add(int(str(N) * i))
        
        for j in range(1, i):
            for k in dp[j]:
                for l in dp[i - j]:
                    v.add(k + l)
                    v.add(k - l)
                    v.add(k * l)
                    if k != 0 and l != 0:
                        v.add(k // l)
        
        if number in v:
            return i
        
    return -1