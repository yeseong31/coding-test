def solution(sizes):
    for i in range(len(sizes)):
        sizes[i][0], sizes[i][1] = max(sizes[i]), min(sizes[i])
            
    return sorted(list(zip(*sizes))[0])[-1] * sorted(list(zip(*sizes))[1])[-1]
