def solution(routes):
    answer = 0
    routes.sort(key=lambda x: -x[1])

    while routes:
        # 단속 카메라 설치
        target = routes.pop()[1]
        answer += 1
        # 단속 대상 확인
        i = 0
        while routes and i < len(routes):
            if routes and routes[i][0] <= target <= routes[i][1]:
                routes.pop(i)
            else:
                i += 1

    return answer


# 다른 풀이 ----------
def solution2(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])

    point = -30001
    for rs, re in routes:
        if point < rs:
            answer += 1
            point = re

    return answer


routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))
