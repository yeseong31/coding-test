def solution(bandage, health, attacks):
    time = 0
    index = 0
    max_health = health
    continuous = 0

    while index < len(attacks):
        time += 1

        if attacks[index][0] != time:
            health += bandage[1]
            continuous += 1

            if continuous == bandage[0]:
                health += bandage[2]
                continuous = 0
            if health > max_health:
                health = max_health
        
        else:
            health -= attacks[index][1]
            index += 1
            
            if health <= 0:
                return -1
            
            continuous = 0

    return health
