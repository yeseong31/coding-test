"""
병사 배치하기(380p)
"""

# 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치하고자 함
# 배치 과정에서는 특정 위치의 병사를 열외시키는 방법을 이용함
# 남아있는 병사의 수는 최대가 되도록 하고 싶음

# '가장 긴 증가하는 부분 수열(LIS)'을 찾는 문제

n = int(input())
lst = list(map(int, input().split()))
lst.reverse()

# d[i]: lst[i]를 마지막 원소로 가지는 부분 수열의 최댓값
d = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if lst[i] > lst[j]:
            d[i] = max(d[i], d[j] + 1)

print(n - max(d))


# Input:
# 6
# 10 20 10 30 20 50
# Output:
# 4
