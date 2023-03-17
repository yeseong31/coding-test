def solution(n):
    def hanoi(n, s, e, m, ans):
        if n == 1:
            return ans.append([s, e])
        
        hanoi(n - 1, s, m, e, ans)
        ans.append([s, e])
        hanoi(n - 1, m, e, s, ans)
    
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer