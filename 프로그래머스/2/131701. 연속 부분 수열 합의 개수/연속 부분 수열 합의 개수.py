def solution(elements):
    answer = set()
    length = len(elements)
    elements *= 2
    
    for i in range(length):
        for j in range(1, length + 1):
            answer.add(sum(elements[i:i + j]))

    return len(answer)
