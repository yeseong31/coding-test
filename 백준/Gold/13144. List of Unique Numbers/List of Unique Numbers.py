answer = 0
n = int(input())
lst = list(map(int, input().split()))

check = [0] * 100001

left = right = 0
while right < n:
    check[lst[right]] += 1
    answer += right - left + 1
    while right < n - 1 and check[lst[right + 1]] > 0:
        check[lst[left]] -= 1
        left += 1
    right += 1

print(answer)