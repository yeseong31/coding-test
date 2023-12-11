from itertools import permutations


def solution(n, weak, dist):
    answer = len(dist) + 1
    length = len(weak)
    
    weak += [x + n for x in weak]
    friends = list(permutations(dist, len(dist)))
    
    for i in range(length):
        for friend in friends:
            cnt = 1        
            check = weak[i] + friend[cnt - 1]
            
            for j in range(i, i + length):
                if check < weak[j]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    check = weak[j] + friend[cnt - 1]
            
            answer = min(answer, cnt)
            
    return answer if answer <= len(dist) else -1
