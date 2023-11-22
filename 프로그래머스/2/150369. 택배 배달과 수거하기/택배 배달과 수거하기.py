def solution(cap, n, deliveries, pickups):
    
    def find_last_index(houses):
        while houses and houses[-1] == 0:
            houses.pop()
        return len(houses) - 1
    
    def find_next_index(houses, index):
        amount = 0
        while index >= 0 and amount + houses[index] <= cap:
            amount += houses[index]
            houses[index] = 0
            index -= 1
        
        houses[index] = houses[index] - (cap - amount)
        return index
    
    def calculate_distance(index1, index2):
        return (max(index1, index2) + 1) * 2
    
    
    answer = 0
    
    delivery_index = find_last_index(deliveries)
    pickup_index = find_last_index(pickups)
    
    answer += calculate_distance(delivery_index, pickup_index)
    
    while (delivery_index >= 0 or pickup_index >= 0):
        delivery_index = find_next_index(deliveries, delivery_index)
        pickup_index = find_next_index(pickups, pickup_index)

        answer += calculate_distance(delivery_index, pickup_index)
    
    return answer