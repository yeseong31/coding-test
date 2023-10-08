n = int(input())
answer = list(map(int, input().split()))
s = int(input())

for i in range(n - 1):
    if s == 0:
        break

    _max, _min = answer[i], min(n, i + 1 + s)
    x = i
    
    for j in range(i + 1, _min):
        if _max < answer[j]:
            _max = answer[j]
            x = j
        
    s -= x - i
    for j in range(x, i, -1):
        answer[j] = answer[j - 1]
    answer[i] = _max
    
print(*answer)
