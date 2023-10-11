s = input()
t = input()

cnt = 0
l = [0] * len(t)
t_set = set(t)

for x in s:
    if x not in t_set:
        continue
    if x == t[0]:
        l[0] += 1
        continue
    idx = t.find(x)
    if l[idx - 1]:
        l[idx - 1] -= 1
        l[idx] += 1

print(l[-1])