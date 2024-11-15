n = list(map(int, input()))
mid = len(n) // 2
print('LUCKY') if sum(n[:mid]) == sum(n[mid:]) else print('READY')