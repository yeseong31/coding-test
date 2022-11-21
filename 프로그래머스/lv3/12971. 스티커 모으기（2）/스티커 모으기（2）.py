def solution(sticker):
    length = len(sticker)
    if length <= 2:
        return max(sticker)
    
    dp1, dp2 = [0] * length, [0] * length
    dp1[0], dp1[1] = sticker[0], max(sticker[0], sticker[1])
    dp2[1], dp2[2] = sticker[1], max(sticker[1], sticker[2])
    
    for i in range(2, length - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])
        dp2[i + 1] = max(dp2[i], dp2[i - 1] + sticker[i + 1])
    
    return max(dp1[-2], dp2[-1])
