# 나머지 합

n, m = map(int, input().split())
nums = list(map(int, input().split())) + [0]
count = [0] * m

# 구간 합 계산
for i in range(n):
    nums[i] += nums[i - 1]
    # 나머지가 같은 수 카운트
    count[nums[i] % m] += 1

# 나머지가 0인 수는 혼자로도 합계를 만족할 수 있음
answer = count[0]
# n개의 수로 합계 만족하는 경우: n * (n - 1) // 2
for c in count:
    answer += c * (c - 1) // 2
print(answer)
