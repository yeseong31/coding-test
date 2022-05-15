# 풀이 1 - 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈

def productExceptSelf(nums: list[int]) -> list[int]:
    out = []
    p = 1
    # 왼쪽 곱셈
    for i in range(len(nums)):
        out.append(p)
        p *= nums[i]
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    p = 1
    for i in range(len(nums) - 1, 0 - 1, -1):
        out[i] *= p
        p *= nums[i]
    return out
