from collections import defaultdict


def solution(answers):
    persons = (
        (1, 2, 3, 4, 5),
        (2, 1, 2, 3, 2, 4, 2, 5),
        (3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
    )
    count = defaultdict(int)
    
    for i in range(3):
        for j, answer in enumerate(answers):
            if persons[i][j % len(persons[i])] == answer:
                count[i + 1] += 1
    
    max_count = max(value for value in count.values())
    return [int(key) for key, value in count.items() if value == max_count]