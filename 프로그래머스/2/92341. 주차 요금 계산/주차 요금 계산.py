from collections import defaultdict
from math import ceil


def convert_time(time):
    return int(time[:2]) * 60 + int(time[3:])


def calculate_fee(duration, fees):
    if duration <= fees[0]:
        return fees[1]

    return fees[1] + ceil((duration - fees[0]) / fees[2]) * fees[3]


def solution(fees, records):
    history = defaultdict(int)
    accumulate_time = defaultdict(int)
    total_fee = defaultdict(int)
    
    close_time = convert_time("23:59")

    for record in records:
        time, car_number, condition = record.split(' ')
        time = convert_time(time)

        if condition == 'IN':
            history[car_number] = time
            continue

        accumulate_time[car_number] += time - history[car_number]
        del history[car_number]
    
    for car_number in history:
        accumulate_time[car_number] += close_time - history[car_number]
        
    for car_number in accumulate_time:
        total_fee[car_number] = calculate_fee(accumulate_time[car_number], fees)

    return [value for _, value in sorted(total_fee.items())]
