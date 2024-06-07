def solution(ingredient):
    answer = 0
    stack = []

    for v in ingredient:
        if v != 1 or stack[-3:] != [1, 2, 3]:
            stack.append(v)
            continue
        for _ in range(3):
            if stack:
                stack.pop()
        answer += 1

    return answer
