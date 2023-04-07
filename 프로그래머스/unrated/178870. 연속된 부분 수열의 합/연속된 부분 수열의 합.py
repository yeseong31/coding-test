def solution(sequence, k):
    answer = [0, len(sequence)]
    l, s = 0, 0

    for r in range(len(sequence)):
        s += sequence[r]
        while l <= r and s >= k:
            if s == k and answer[1] - answer[0] > r - l:
                answer = l, r
            s -= sequence[l]
            l += 1
        
    return answer