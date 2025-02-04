def hanoi(n, start, mid, end):
    if n < 1:
        return
    global count, arr
    hanoi(n - 1, start, end, mid)
    arr.append((start, end))
    count += 1
    hanoi(n - 1, mid, start, end)

n = int(input())
count = 0
arr = []

hanoi(n, 1, 2, 3)
print(count)
for a, b in arr:
    print(a, b)