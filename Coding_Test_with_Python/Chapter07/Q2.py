# 실전 문제 - 떡볶이 떡 만들기(201p)

# 떡의 개수 N, 요청한 떡의 길이 M
n, m = map(int, input().split())
data = list(map(int, input().split()))


def search(array, start, end):
    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for d in data:
            if d > mid:
                total += d - mid
        # 잘리고 남은 떡의 총 길이가 m보다 작으면...
        if total < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result


print(search(data, 0, max(data)))
