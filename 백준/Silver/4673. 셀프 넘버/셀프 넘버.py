def d(n):
    a = 0
    for i in list(str(n)):
        a += int(i) 
    return int(n) + a
self_number = []
for i in range(1,10001):
    k = d(i)
    self_number.append(k)

for i in range(1, 10001):
    if i in self_number:
        pass
    else:
        print(i)