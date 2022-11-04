def check(arr, k):
    arr.sort()
    return sum([arr[i] for i in range(len(arr) - 1, -1, -k)]) * 2


n, m = map(int, input().split())
books = list(map(int, input().split()))

left = [-i for i in books if i < 0]
right = [i for i in books if i > 0]

answer = check(left, m) + check(right, m)
answer -= max(left + right)
print(answer)