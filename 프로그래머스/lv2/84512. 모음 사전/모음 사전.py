from itertools import product

def solution(word):
    data = sorted([''.join(p) for i in range(5) for p in product('AEIOU', repeat=i + 1)])
    return data.index(word) + 1