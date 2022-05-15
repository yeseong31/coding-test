"""
고정점 찾기 (368p)
- 값이 인덱스와 동일한 원소
"""


def binary_search(start, end):
    # 탈출 조건: 찾는 원소가 없다면 return -1
    if start > end:
        return -1

    mid = (start + end) // 2
    # print(f'mid = {mid}')

    # 고정점이 있다면
    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        return binary_search(mid + 1, end)
    else:
        return binary_search(start, mid - 1)


n = int(input())
arr = list(map(int, input().split()))

# 처음 idx은 arr의 중간 값
print(binary_search(0, n - 1))
