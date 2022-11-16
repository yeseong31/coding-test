from collections import defaultdict, Counter


def solution(genres, plays):
    answer = []
    total = defaultdict(int)
    musics = defaultdict(list)
    for i, (g, p) in enumerate(zip(genres, plays)):
        total[g] += p
        musics[g].append((p, i))
    for k in sorted(total, key=lambda x: -total[x]):
        answer += [v[1] for v in sorted(musics[k], key=lambda x: -x[0])[:2]]
    return answer