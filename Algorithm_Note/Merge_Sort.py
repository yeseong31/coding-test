def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    result.extend([*left, *right])
    return result


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:]),
    return merge(left, right)


print(merge_sort([3, 0, 1, 8, 7, 2, 5, 4, 6, 9]))
