import sys

input = sys.stdin.readline

n, c = map(int, input().split())
houses = sorted([int(input()) for _ in range(n)])

# 최대 간격, 최소 간격
left, right = 1, houses[-1] - houses[0]
result = 0

while left <= right:
    # 간격을 이진 탐색을 이용하여 조절
    mid = (left + right) // 2
    # 설치할 공유기 수 카운트
    cnt = 1
    # 설치 장소
    check = houses[0]

    for i in range(1, n):
        # 정해진 기준(간격)을 만족한다면
        if mid <= houses[i] - check:
            cnt += 1
            check = houses[i]
    # 공유기를 c개 이상 설치했다면
    if cnt >= c:
        left = mid + 1
        result = mid
    else:
        right = mid - 1

print(result)


# 아래 주석 처리된 코드는 '메모리 제한'으로 인해 실패한 코드
# distance = 0
# for comb in list(itertools.combinations(houses, c)):
#     dist = int(1e9)
#     p = comb[0]
#     for i in comb[1:]:
#         dist = min(dist, i - p)
#         p = i
#     distance = max(distance, dist)
# print(distance)
