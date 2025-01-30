def solution(mats, park):
    answer = set()
    n, m = len(park), len(park[0])
    
    expanded_park = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for x in range(n + 1):
        expanded_park[x][0] = 1
    for y in range(m + 1):
        expanded_park[0][y] = 1
    
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if park[x - 1][y - 1] != '-1':
                continue
            elif x == 1 or y == 1:
                expanded_park[x][y] = 1
                answer.add(1)
                continue
            
            a, b, c = expanded_park[x - 1][y - 1], expanded_park[x][y - 1], expanded_park[x - 1][y]
            
            if a != 0 and b != 0 and c != 0:
                expanded_park[x][y] = min(a, b, c) + 1
                answer.add(expanded_park[x][y])
            else:
                expanded_park[x][y] = 1
                answer.add(1)
    
    common_numbers = answer.intersection(mats)
    return max(common_numbers) if common_numbers else -1
