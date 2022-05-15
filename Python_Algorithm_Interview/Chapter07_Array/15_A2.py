# 투 포인터로 합 계산

def threeSum(nums: list[int]) -> list[list[int]]:
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 간격을 좁혀가며 합 sum 계산
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum_values = nums[i] + nums[left] + nums[right]
            if sum_values < 0:
                left += 1
            elif sum_values > 0:
                right -= 1
            else:
                result.append((nums[i], nums[left], nums[right]))
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return result
