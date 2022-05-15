# 풀이 2 - 저점과 현재 값과의 차이 계산
import sys


def maxProfit(prices: list[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    # 최솟값과 최댓값을 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, min_price - price)
    return profit
