from collections import defaultdict


def solution(genres, plays):
    answer = []
    total_play = defaultdict(int)
    genre_list = defaultdict(list)
    
    for i, (play, genre) in enumerate(zip(plays, genres)):
        total_play[genre] += play
        genre_list[genre].append((play, i))
    
    for k in sorted(total_play, key=lambda x: total_play[x], reverse=True):
        for g in sorted(genre_list[k], key=lambda x: (-x[0], x[1]))[:2]:
            answer.append(g[1])
        
    return answer