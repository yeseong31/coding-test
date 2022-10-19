# 잃어버린 괄호

exp = input().split('-')
answer = 0
for i in exp[0].split('+'):
    answer += int(i)
for i in exp[1:]:
    for j in i.split('+'):
        answer -= int(j)
print(answer)
