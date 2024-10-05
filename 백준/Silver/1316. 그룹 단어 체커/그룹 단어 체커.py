n = int(input())

array = []
for _ in range(n):
    array.append(input())
    
result = 0
for word in array:
    check = [0] * 26
    c = int(ord(word[0])) - int(ord('a'))
    check[c] = n = 1
    for i in range(1, len(word)):
        prev = int(ord(word[i - 1])) - int(ord('a'))
        cur = int(ord(word[i])) - int(ord('a'))
        if prev != cur and check[cur] == 0:
            check[cur] = 1
        elif prev == cur:
            continue
        else:
            n = 0
    result += n
    
print(result) 