# 풀이 1 - 브루트 포스로 계산
# ...타임아웃으로 풀리지 않음

def maxProfit(prices: list[int]) -> int:
    max_price = 0
    for i, n in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(max_price, prices[j] - n)
    return max_price
