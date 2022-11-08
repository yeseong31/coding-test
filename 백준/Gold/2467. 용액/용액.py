import sys


def solution():
    _ = int(input())
    lst = list(map(int, input().split()))
    
    left, right = 0, len(lst) - 1
    x = y = -1
    _min = sys.maxsize
    
    while left < right:
        target = lst[left] + lst[right]
        if abs(target) <= _min:
            _min = abs(target)
            x, y = left, right
        if target == 0:
            break
        elif target < 0:
            left += 1
        else:
            right -= 1
    
    print(f'{lst[x]} {lst[y]}')


solution()