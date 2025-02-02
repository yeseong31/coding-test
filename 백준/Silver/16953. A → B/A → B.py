answer = 1
a, b = input().split()

while b and b != '1':
    if b == a:
        break
    if b[-1] == '1':
        b = b[:-1]
    elif int(b) % 2 == 0:
        b = str(int(b) // 2)
    else:
        break

    answer += 1

print(answer if b == a else -1)