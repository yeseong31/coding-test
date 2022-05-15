# 주식을 사고팔기 가장 좋은 시점(195p)

def maxProfit(prices: list[int]) -> int:
    price = 0
    min_value = int(1e9)
    for p in prices:
        min_value = min(min_value, p)
        price = max(price, p - min_value)
    return price


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))

prices = [7, 6, 4, 3, 1]
print(maxProfit(prices))
