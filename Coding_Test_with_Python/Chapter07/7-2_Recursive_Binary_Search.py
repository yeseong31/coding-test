# 재귀 함수로 구현한 이진 탐색
# O(logN)

def recursive_binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif target < array[mid]:
        return recursive_binary_search(array, target, start, mid - 1)
    else:
        return recursive_binary_search(array, target, mid + 1, end)


# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, t = list(map(int, input().split()))
# 전체 원소 입력받기
arr = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = recursive_binary_search(arr, t, 0, n - 1)
if result is None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)
