from collections import defaultdict


def solution():
    r, c = map(int, input().split())
    s = [input() for _ in range(r)]
    answer = 0
    left, right = 0, r - 1
    
    while left <= right:
        mid = (left + right) // 2
        check = True
        dic = defaultdict(int)
        
        for j in range(c):
            target = ''.join(s[i][j] for i in range(mid, r))
            if dic[target]:
                check = False
                break
            dic[target] += 1
            
        if check:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
        
    return answer


print(solution())
