def solution(sticker):
    length = len(sticker)

    if length <= 2:
        return max(sticker)

    d1 = [0] * length
    d2 = [0] * length
    d1[0], d1[1] = sticker[0], max(sticker[0], sticker[1])
    d2[1], d2[2] = sticker[1], max(sticker[1], sticker[2])
    for i in range(2, length - 1):
        d1[i] = max(d1[i - 1], d1[i - 2] + sticker[i])
        d2[i + 1] = max(d2[i], d2[i - 1] + sticker[i + 1])

    return max(d1[-2], d2[-1])


sticker = [5, 1, 16, 17, 16]
print(solution(sticker))
