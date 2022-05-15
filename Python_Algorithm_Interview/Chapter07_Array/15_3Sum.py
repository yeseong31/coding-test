# 세 수의 합(184p)
# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라

def threeSum(nums: list[int]) -> list[list[int]]:
    if not nums:
        return []

    nums.sort()
    answer = []

    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # 투 포인터로 계산
        left, right = i + 1, len(nums) - 1
        # 범위 안에서만
        while left < right:
            sum_of_value = nums[i] + nums[left] + nums[right]
            # 합한 값이 0보다 작다면 left 이동
            if sum_of_value < 0:
                left += 1
            # 합한 값이 0보다 크다면 right 이동
            elif sum_of_value > 0:
                right -= 1
            # 그렇지 않다면... 정답 처리 및 후처리
            else:
                answer.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return answer


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))

nums = [0]
print(threeSum(nums))

nums = []
print(threeSum(nums))
