n = int(input())
numbers = [[0, False] for _ in range(10)]
answer = 0

for _ in range(n):
    s = input()
    m = 1
    numbers[ord(s[0]) - 65][1] = True
    
    for c in range(len(s) - 1, -1, -1):
        numbers[ord(s[c]) - 65][0] += m
        m *= 10

numbers.sort(reverse=True)

if numbers[9][1]:
    for i in range(8, -1, -1):
        if not numbers[i][1]:
            del numbers[i]
            break

for i in range(9):
    answer += numbers[i][0] * (9 - i)

print(answer)
