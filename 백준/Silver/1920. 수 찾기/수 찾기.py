def binary_search(x, left, right):
    while left <= right:
        mid = (left + right) // 2
        if x == numbers[mid]:
            return 1
        if x < numbers[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return 0


n = int(input())
numbers = sorted(list(map(int, input().split())))
start, end = numbers[0], numbers[-1]

_ = int(input())
for target in list(map(int, input().split())):
    print(binary_search(target, 0, n - 1))