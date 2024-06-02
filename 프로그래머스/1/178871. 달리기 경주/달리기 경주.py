def solution(players, callings):
    ranks = {v: i for i, v in enumerate(players)}
    
    for call in callings:
        i = ranks[call]
        ranks[call] -= 1
        ranks[players[i - 1]] += 1
        players[i - 1], players[i] = players[i], players[i - 1]
        
    return players
