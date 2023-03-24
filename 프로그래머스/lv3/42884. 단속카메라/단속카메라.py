def solution(routes):
    answer = 0
    routes.sort()
    while routes:
        target = routes.pop()[0]
        while routes and routes[-1][0] <= target <= routes[-1][1]:
            routes.pop()
        answer += 1
    return answer