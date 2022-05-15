# 파이썬에서는 '이진 탐색'을 쉽게 구현할 수 있도록 bisect 라이브러리를 제공한다.

# bisect
# '정렬된 배열'에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용된다.

# bisect_left(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾음
# bisect_right(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾음
#     * 이 두 함수는 시간 복잡도 O(logN)에서 동작한다.

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

# bisect_left() 함수와 bisect_right() 함수는 '정렬된 리스트'에서 '값이 특정 번위에 속하는 원소의 개수'를 구할 때 유용하다.


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
# 값이 4인 데이터 수 출력
print("값이 4인 데이터 수: ", count_by_range(a, 4, 4))
# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print("값이 [-1, 3] 범위에 있는 데이터 수: ", count_by_range(a, -1, 3))