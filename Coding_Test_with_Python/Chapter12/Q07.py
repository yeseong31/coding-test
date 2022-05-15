# 럭키 스트레이트(321p)

# 현재 캐릭터의 점수 n
n = list(input())
p = len(n) // 2

sum_values = 0
for i in n[:p]:
    sum_values += int(i)
for i in n[p:]:
    sum_values -= int(i)

if sum_values == 0:
    print('LUCKY')
else:
    print('READY')
