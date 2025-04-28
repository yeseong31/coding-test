def solution(s):
    numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    for seq, number in enumerate(numbers):
        s = s.replace(number, str(seq))
    return int(s)
