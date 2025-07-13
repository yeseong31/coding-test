def solution(sequence):
    prefix_sums = [0]

    for i, num in enumerate(sequence):
        sign = 1 if i % 2 == 0 else -1
        prefix_sums.append(prefix_sums[-1] + num * sign)

    return max(prefix_sums) - min(prefix_sums)