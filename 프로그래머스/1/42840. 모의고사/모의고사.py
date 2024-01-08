def solution(answers):
    persons = (
        (1, 2, 3, 4, 5),
        (2, 1, 2, 3, 2, 4, 2, 5),
        (3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
    )
    
    count = [0, 0, 0]
    
    for i in range(len(answers)):
        for j in range(len(persons)):
            if persons[j][i % len(persons[j])] == answers[i]:
                count[j] += 1
    
    return [i + 1 for i in range(len(count)) if count[i] == max(count)]
