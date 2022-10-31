def solution(distance, scope, times):
    answer = distance

    for i in range(len(times)):
        check = 'o' * times[i][0] + 'x' * times[i][1]
        left, right = sorted(scope[i])
        target = left % sum(times[i])
        
        for step in range(right - left + 1):
            if check[target - 1] == 'o':
                answer = min(answer, left + step)
            target = target + 1 if target < len(check) else 1

    return answer