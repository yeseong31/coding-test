def solution(n: int):
    primes = [True for _ in range(n + 1)]

    for i in range(2, int((n + 1) ** 0.5) + 1):
        if primes[i]:
            for j in range(2 * i, (n + 1), i):
                primes[j] = False
    primes = [x for x, v in enumerate(primes) if v and x >= 2]

    part_sum = [0] * (len(primes) + 1)
    for i in range(len(primes)):
        part_sum[i+1] = part_sum[i] + primes[i]

    answer = 0
    left, right = 0, 1

    while right < len(part_sum):
        target = part_sum[right] - part_sum[left]
        if target == n:
            answer += 1
        if target >= n:
            left += 1
        else:
            right += 1

    return answer


print(solution(int(input())))