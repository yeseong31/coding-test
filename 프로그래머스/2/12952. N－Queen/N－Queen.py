def solution(n):
    def queens(x):
        if x == n + 1:
            return 1
        
        ans = 0
        for i in range(1, n + 1):
            a, b = x + i, n + x - i
            
            if not (col[i] or d1[a] or d2[b]):
                col[i] = d1[a] = d2[b] = True
                ans += queens(x + 1)
                col[i] = d1[a] = d2[b] = False
        
        return ans

    col, d1, d2 = [False] * (n + 1), [False] * (2 * n + 1), [False] * (2 * n + 1)
    return queens(1)