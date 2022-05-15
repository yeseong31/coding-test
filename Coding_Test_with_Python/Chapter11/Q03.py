# 문자열 뒤집기(313p)

s = input()

# 0으로 뒤집는 경우와 1로 뒤집는 경우를 나누어 생각해봐야 할 듯
count_0 = 0
count_1 = 0

# 0으로 뒤집는 경우
flag = 0
for i in s:
    if int(i) == 1 and flag != 1:
        count_0 += 1
        flag = 1
    elif int(i) == 0:
        count_1 += 1

# 1로 뒤집는 경우
flag = 0
for i in s:
    if int(i) == 0 and flag != 1:
        count_1 += 1
        flag = 1
    elif int(i) == 1:
        flag = 0

print(min(count_0, count_1))
