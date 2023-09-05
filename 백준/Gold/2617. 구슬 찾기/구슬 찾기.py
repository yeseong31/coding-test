from collections import defaultdict


def solution():
    answer = 0
    heavy, light = defaultdict(set), defaultdict(set)

    for a, b in results:
        heavy[a].add(b)
        light[b].add(a)

    for i in range(1, n + 1):
        for h in heavy[i]:
            light[h].update(light[i])
        for l in light[i]:
            heavy[l].update(heavy[i])

    for i in range(1, n + 1):
        if len(heavy[i]) >= (n + 1) // 2 or len(light[i]) >= (n + 1) // 2:
            answer += 1
    return answer


n, m = map(int, input().split())
results = [(map(int, input().split())) for _ in range(m)]
print(solution())