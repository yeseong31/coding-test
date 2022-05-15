"""
국영수 (359p)
"""


n = int(input())

data = []
for _ in range(n):
    name, kor, eng, math = input().split()
    data.append((name, int(kor), int(eng), int(math)))

for res, _, _, _ in sorted(data, key=lambda x: (-x[1], x[2], -x[3], x[0])):
    print(res)
