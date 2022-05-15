# 문자열 재정렬(322p)

s = input()

# 문자 정렬 + 숫자 합
alpha, num = [], 0
for i in s:
    if i.isalpha():
        alpha.append(i)
    elif i.isdigit():
        num += int(i)

alpha.sort()

result = ''.join(alpha)
if num != 0:
    result += str(num)
print(result)

# 입력 예시
# K1KA5CB7
# 출력 예시
# ABCKK13
