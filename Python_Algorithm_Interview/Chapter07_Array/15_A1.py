# 풀이 1 - 브루토 포스로 계산
# ...타임아웃으로 풀이에 실패하는 방법이므로 다른 방법을 찾아야 함

def threeSum(nums: list[int]) -> list[list[int]]:
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        # 중복된 값은 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])

    return result

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

nums = [0]
print(threeSum(nums))

nums = []
print(threeSum(nums))
