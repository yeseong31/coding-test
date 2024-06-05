import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

sum_list = [0]
total = 0

for i in nums:
    sum_list.append(total := total + i)

for _ in range(m):
    left, right = map(int, input().split())
    print(sum_list[right] - sum_list[left - 1])
