from itertools import combinations


def solution(relation):
    row_count = len(relation)
    col_count = len(relation[0])

    candidate_keys = []

    for size in range(1, col_count + 1):
        for cols in combinations(range(col_count), size):
            if any(set(key).issubset(cols) for key in candidate_keys):
                continue

            projected = {tuple(row[i] for i in cols) for row in relation}
            if len(projected) == row_count:
                candidate_keys.append(cols)

    return len(candidate_keys)