# 게수 정렬을 이용한 풀이

n = int(input())
count = [0] * 1000001

for i in input().split():
    count[int(i)] += 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if count[i] > 0:
        print('yes', end=' ')
    else:
        print('no', end=' ')
