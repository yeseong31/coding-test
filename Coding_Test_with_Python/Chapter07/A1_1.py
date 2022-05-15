# 이진 탐색(반복문)

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(arr, i, 0, n - 1)
    if result is not None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
