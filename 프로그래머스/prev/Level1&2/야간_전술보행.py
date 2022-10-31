def solution(distance, scope, times):
    for i, s in enumerate(scope):
        s.sort()
        for p in range(s[0], s[1] + 1):
            if 1 <= p % sum(times[i]) <= times[i][0]:
                distance = min(distance, p)
                break

    return distance


# 첫 번째 풀이
# def solution(distance, scope, times):
#     for i in range(len(times)):
#         rule = [True] * times[i][0] + [False] * times[i][1]
#         l, r = sorted(scope[i])
#         s = l % sum(times[i])
#
#         for step in range(r - l + 1):
#             if rule[s - 1]:
#                 distance = min(distance, l + step)
#             s = s + 1 if s < len(rule) else 1
#
#     return distance


print(solution(10, [[3, 4], [5, 8]], [[2, 5], [4, 3]]))
print(solution(12, [[7, 8], [4, 6], [11, 10]], [[2, 2], [2, 4], [3, 3]]))
