# 배열 파티션 I(190p)

# n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.

def arrayPairSum(nums: list[int]) -> int:
    return sum(sorted(nums)[::2])
