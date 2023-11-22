from itertools import product


def solution(users, emoticons):
    
    def calculate_discount_price(discount_rate, index):
        return emoticons[index] * (100 - discount_rate) // 100
    
    def check_service(discount_rates):
        subscribers = 0
        total_price = 0
        
        for wanted_rate, price in users:
            sum_value = 0
            
            for index, discount_rate in enumerate(discount_rates):
                if wanted_rate <= discount_rate:
                    sum_value += calculate_discount_price(discount_rate, index)
                if sum_value >= price:
                    subscribers += 1
                    sum_value = 0
                    break
            
            total_price += sum_value            
        
        return subscribers, total_price
    
    return max(check_service(rate) for rate in product((10, 20, 30, 40), repeat=len(emoticons)))
        