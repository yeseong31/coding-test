def solution(prices):
    answer = []
    n = len(prices)
    for i in range(n):
        for j in range(i, n):
            if prices[i] > prices[j]:
                break
        answer.append(j - i)
    return answer