def solution(cap, n, deliveries, pickups):
    answer = 0
    d = p = 0
    point = n - 1

    for i in range(n - 1, -1, -1):
        d += deliveries[i]
        p += pickups[i]

        while d > cap or p > cap:
            d -= cap
            p -= cap
            answer += 2 * (point + 1)
            point = i

    if d > 0 or p > 0:
        answer += 2 * (point + 1)

    return answer
