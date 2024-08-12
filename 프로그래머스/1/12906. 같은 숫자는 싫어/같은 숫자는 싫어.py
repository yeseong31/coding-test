def solution(arr):
    return [a for i, a in enumerate(arr) if i == 0 or a != arr[i - 1]]