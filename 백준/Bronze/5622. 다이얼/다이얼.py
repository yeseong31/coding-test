word = input().lower()
num = [0, 0, 0, 3, 3, 3, 3, 3, 4, 3, 4]
alphabet = 'abcdefghijklmnopqrstuvwxyz'

dial = []
start = 0
for n in num:
    tmp = alphabet[start:start + n]
    dial.append(tmp)
    start += n

result = 0
for w in word:
    for i in range(3, len(dial)):
        if w in dial[i]:
            result += i
print(result)