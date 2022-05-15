# 곱하기 혹은 더하기(312p)

s = input()
result = int(s[0])

for i in s[1:]:
    if result <= 1 or int(i) <= 1:
        result += int(i)
    else:
        result *= int(i)

print(result)
