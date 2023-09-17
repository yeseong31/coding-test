s = input().lower()
count = [0] * 27
alpha = 'abcdefghijklmnopqrstuvwxyz'

maxIndex = 0
for i in s:
    i = int(ord(i)) - int(ord('a')) + 1
    count[i] += 1
    if count[maxIndex] < count[i]:
        maxIndex = i

count.sort()
if count[-1] == count[-2]:
    print('?')
else:
    print(alpha[maxIndex - 1].upper())
