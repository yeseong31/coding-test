from collections import defaultdict


def solution(genres, plays):
    answer = []

    total_play = defaultdict(int)
    song = defaultdict(list)

    for i, (genre, play) in enumerate(zip(genres, plays)):
        total_play[genre] += play
        song[genre].append((i, play))

    for k, v in sorted(total_play.items(), key=lambda x: x[1], reverse=True):
        for i, p in sorted(song[k], key=lambda x: x[1], reverse=True)[:2]:
            answer += [i]

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))