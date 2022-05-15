# 자신을 제외한 배열의 곱(193p)

# 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.
# 나눗셈을 하지 않고 O(N)으로 풀 것

def productExceptSelf(nums: list[int]) -> list[int]:
    n = 1
    result = [n]
    for i in range(len(nums) - 1):
        result.append(result[-1] * nums[i])
    for i in range(len(nums) - 1, 0, -1):
        result[i - 1] *= n * nums[i]
        n *= nums[i]
    return result


nums = [1,2,3,4]
print(productExceptSelf(nums))

nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))
