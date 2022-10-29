# 친구 추천 알고리즘
from collections import defaultdict


def solution(user: str, friends: list[list[str]], visitors: list[str]) -> list[str]:
    graph = defaultdict(set)
    points = defaultdict(int)

    for u1, u2 in friends:
        graph[u1].add(u2)
        graph[u2].add(u1)
        points[u1] = points[u2] = 0

    for visitor in visitors:
        points[visitor] += 1
        for target in graph[visitor]:
            if target != user:
                points[target] += 10

    result = []
    for name in sorted(points, key=lambda x: (-points[x], x)):
        if name != user and name not in graph[user] and points[name] > 0:
            result.append(name)
    return result


user = 'mrko'
friends = [["donut", "andole"], ["donut", "jun"], ["donut", "mrko"], ["shakevan", "andole"], ["shakevan", "jun"],
           ["shakevan", "mrko"]]
visitors = ["bedi", "bedi", "donut", "bedi", "shakevan"]
print(solution(user, friends, visitors))  # ['andole', 'jun', 'bedi']
