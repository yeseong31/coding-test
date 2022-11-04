def solution(k, ranges):
    MAX_LEN = 10000
    answer = []
    areas = [0]

    for _ in range(MAX_LEN):
        if k == 1:
            break
        prev = k
        if k % 2 == 0:
            k /= 2
        else:
            k = 3 * k + 1
        areas.append((prev + k) / 2)

    length = len(areas)
    for i in range(2, length):
        areas[i] += areas[i - 1]

    for a, b in ranges:
        b += length - 1
        if b >= length or a > b:
            answer.append(-1.0)
        elif a == b:
            answer.append(0.0)
        else:
            answer.append(areas[b] - areas[a])
    return answer