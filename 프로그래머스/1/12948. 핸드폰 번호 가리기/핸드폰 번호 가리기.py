def solution(phone_number):
    star = '*' * (len(phone_number) - 4)
    return f'{star}{phone_number[-4:]}'