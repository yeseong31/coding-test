# 선택 정렬(Selection Sort) --------------------------------------------------------------------------------------------
# 시간 복잡도: O(N^2)
def selection_sort(array):
    for i in range(len(array)):
        min_value = i
        for j in range(i + 1, len(array)):
            if array[min_value] > array[j]:
                min_index = j
        array[i], array[min_value] = array[min_value]. array[i]

# 삽입 정렬(Insertion Sort) --------------------------------------------------------------------------------------------
# 시간 복잡도: O(N^2)
def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break

# 퀵 정렬(Quick Sort) --------------------------------------------------------------------------------------------------
# 시간 복잡도: O(NlogN)
# 촤악의 경우 시간 복잡도: O(N^2)
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

# 퀵 정렬2(Quick Sort with python adventage) ---------------------------------------------------------------------------
def quick_sort_2(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    return quick_sort_2(left_side) + [pivot] + quick_sort_2(right_side)

# 계수 정렬(Count Sort) ------------------------------------------------------------------------------------------------
# 시간 복잡도: O(N + K) (데이터의 수 N, 데이터 중 최댓값 K)
def count_sort(array):
    count = [0] * (max(array) + 1)
    for i in range(len(array)):
        count[array[i]] += 1
    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')

# 기수 정렬(Radix Sort) ------------------------------------------------------------------------------------------------
from math import log

# 현재 자릿수(d)와 진법(base)에 맞는 숫자 변환
# ex) 102, d = 1, base = 10, : 2
def get_digit(number, d, base):
  return (number // base ** d) % base

# 자릿수 기준으로 counting sort
# A : input array
# position : 현재 자릿수, ex) 102, d = 1 : 2
# base : 10진수라면 base = 10
def counting_sort_with_digit(A, d, base):
    # k : ex) 10진수의 최대값 = 9
    k = base - 1
    B = [-1] * len(A)
    C = [0] * (k + 1)
    # 현재 자릿수를 기준으로 빈도수 세기
    for a in A:
        C[get_digit(a, d, base)] += 1
    # C 업데이트
    for i in range(k):
        C[i + 1] += C[i]
    # 현재 자릿수를 기준으로 정렬
    for j in reversed(range(len(A))):
        B[C[get_digit(A[j], d, base)] - 1] = A[j]
        C[get_digit(A[j], d, base)] -= 1
    return B

def radix_sort(lst, base=10):
    # 입력된 리스트 가운데 최댓값의 자릿수 확인
    digit = int(log(max(lst), base) + 1)
    # 자릿수 별로 counting sort
    for d in range(digit):
        lst = counting_sort_with_digit(lst, d, base)
    return lst

# 병합 정렬(Merge Sort) ------------------------------------------------------------------------------------------------
def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid
        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1
        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1
        for i in range(low, high):
            arr[i] = temp[i - low]
    return sort(0, len(arr))


