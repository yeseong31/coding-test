from math import factorial


def solution(n, k):
    answer = []
    nums = list(range(1, n + 1))
    k -= 1
    
    while nums:
        i, k = divmod(k, factorial(len(nums) - 1))
        answer.append(nums.pop(i))
    
    return answer
