def solution(routes):
    answer = 0
    
    routes.sort(key=lambda x: -x[1])
    while routes:
        end = routes.pop()[1]
        answer += 1
        while routes and routes[-1][0] <= end:
            routes.pop()
    
    return answer