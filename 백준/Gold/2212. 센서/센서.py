n = int(input())
k = int(input())
sensors = sorted(list(map(int, input().split())))

if k >= n:
    print(0)
else:
    distance = sorted([(sensors[i] - sensors[i - 1]) for i in range(1, n)])
    for _ in range(k - 1):
        distance.pop()
    print(sum(distance))