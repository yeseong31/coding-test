from itertools import combinations


def solution(places):
    def check_partition(a, b, partitions):
        x1, y1 = a
        x2, y2 = b
        if x1 == x2 and (x1, (y1 + y2) // 2) in partitions:
            return True
        elif y1 == y2 and ((x1 + x2) // 2, y1) in partitions:
            return True
        elif (x1, y2) in partitions and (x2, y1) in partitions:
            return True
        return False

    def calculate_manhattan_distance(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def check_place(p):
        persons, partitions = [], []
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    persons.append((i, j))
                elif p[i][j] == 'X':
                    partitions.append((i, j))

        comb = list(combinations(persons, 2))
        for a, b in comb:
            manhattan = calculate_manhattan_distance(a, b)
            if manhattan <= 1 or (manhattan == 2 and not check_partition(a, b, partitions)):
                return False
        return True

    answer = []
    for place in places:
        if check_place(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer