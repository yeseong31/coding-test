"""
정렬된 배열에서 특정 수의 개수 구하기 (367p)
"""
from bisect import bisect_left, bisect_right


# 숫자의 개수, 타겟이 되는 수
n, x = map(int, input().split())
# 정렬된 배열
numbers = list(map(int, input().split()))

count = bisect_right(numbers, x) - bisect_left(numbers, x)
if count == 0:
    print(-1)
else:
    print(count)
