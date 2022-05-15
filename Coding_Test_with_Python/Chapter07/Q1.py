# 실전 문제 - 부품 찾기(197p)

# 가게의 부품 수
n = int(input())
# 가게 내 부품 번호
a = sorted(list(map(int, input().split())))
# 손님 확인 부품 수
m = int(input())
# 손님 확인 요청 부품 번호
b = list(map(int, input().split()))


def search(arr, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if arr[mid] == target:
        return True
    elif target < arr[mid]:
        return search(arr, target, start, mid - 1)
    else:
        return search(arr, target, mid + 1, end)


# 손님 확인 요청 부품을 하나씩 살펴보기
for i in b:
    if search(a, i, 0, n):
        print('yes', end=' ')
    else:
        print('no', end=' ')
