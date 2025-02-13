# 인원수, 몇 번째를 없앨까
n, k = map(int, input().split())
result = []
josephus = [i for i in range(1, n + 1)]

idx = k - 1
while josephus:
    if idx >= len(josephus):
        idx %= len(josephus)
    else:
        result.append(str(josephus.pop(idx)))
        idx += k - 1

print('<' + ', '.join(result) +'>', sep='')
        
#     @     @     @     @     @     @     @
# 1 2 3 4 5 6 7 1 2 4 5 7 1 4 5 1 4 1 4 4 4