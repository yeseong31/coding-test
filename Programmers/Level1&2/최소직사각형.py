def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]

    return sorted(list(zip(*sizes))[0])[-1] * sorted(list(zip(*sizes))[1])[-1]
