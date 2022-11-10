from collections import defaultdict

members = defaultdict(list[str])
names = defaultdict(str)

n, m = map(int, input().split())
for _ in range(n):
    group = input()
    for _ in range(int(input())):
        name = input()
        members[group].append(name)
        names[name] = group
    members[group].sort()
for _ in range(m):
    name = input()
    if int(input()) == 1:
        print(names[name])
        continue
    for x in members[name]:
        print(x)