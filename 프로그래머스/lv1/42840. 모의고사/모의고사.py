def solution(answers):
    count = [0, 0, 0]
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i, v in enumerate(answers):
        if student1[i % 5] == v:
            count[0] += 1
        if student2[i % 8] == v:
            count[1] += 1
        if student3[i % 10] == v:
            count[2] += 1
            
    return [i for i, v in enumerate(count, 1) if v == max(count)]