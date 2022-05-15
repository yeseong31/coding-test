# 예제 B-2 암호 만들기(486p)

from itertools import combinations

# 암호 길이, 문자 개수
l, c = map(int, input().split())
vowel = ['a', 'e', 'i', 'o', 'u']

data = input().split()
data.sort()

for pw in combinations(data, l):
    cnt = 0
    for i in pw:
        if i in vowel:
            cnt += 1
    # 최소 한 개의 모음과 최소 두 개의 자음
    if cnt >= 1 and l - cnt >= 2:
        print(''.join(pw))
