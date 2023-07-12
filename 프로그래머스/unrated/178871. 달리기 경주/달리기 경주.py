def solution(players, callings):
    ranks = {v: i for i, v in enumerate(players)}
    
    for call in callings:
        i = ranks[call]
        front_name = players[i - 1]
        
        players[i - 1], players[i] = players[i], players[i - 1]
        
        ranks[call] -= 1
        ranks[front_name] += 1
        
    return players