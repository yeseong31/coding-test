"""
공유기 설치 (369p)
"""


# 집의 개수 n, 공유기의 개수 c
n, c = map(int, input().split())
# 집의 좌표
houses = []
for _ in range(n):
    houses.append(int(input()))
houses.sort()

# 집의 좌표 중 가장 작은 값
start = houses[1] - houses[0]
# 집의 좌표 중 가장 큰 값
end = houses[-1] - houses[0]

result = 0

# 이진 탐색
while start <= end:
    mid = (start + end) // 2
    # 기준(초깃값)
    v = houses[0]
    cnt = 1

    # mid 값을 이용하여 앞에서부터 하나씩 공유기 설치
    for i in range(1, n):
        # 공유기 간 거리
        gap = v + mid
        # 공유기 간 거리보다 먼 case를 발견했다면, 공유기 설치
        if houses[i] >= gap:
            v = houses[i]
            cnt += 1

    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)


# 가장 인접한 공유기 간 거리의 최댓값
# v     v     v - 설치
# 1, 2, 4, 8, 9 - 좌표
#   1    7
#    3     5    - 거리
#     7      1

