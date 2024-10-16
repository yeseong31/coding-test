from itertools import combinations

l, c = map(int, input().split())
data = sorted(input().split())

vowels = ['a', 'e', 'i', 'o', 'u']

for pw in combinations(data, l):
    count = 0
    for i in pw:
        if i in vowels:
            count += 1
    if count >= 1 and count <= l - 2:
        print(''.join(pw))
