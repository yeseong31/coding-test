def solution(s):
    answer = s
    number = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0
    }

    for target in number.items():
        answer = answer.replace(target[0], str(target[1]))

    return int(answer)