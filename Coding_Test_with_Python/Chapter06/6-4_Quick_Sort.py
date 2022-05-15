# 퀵 정렬
# 평균 O(NlogN)
# 최악의 경우 O(N^2)... (데이터가 이미 정렬되어 있는 경우)

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while start < right and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


a = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(a, 0, len(a) - 1)
print(a)
