s = input()
count = {'0': 0, '1': 0}
prev = s[0]

for i in range(1, len(s) + 1):
    if i == len(s):
        count[prev] += 1
        break
    if s[i] != prev:
        count[prev] += 1
        prev = s[i]

print(min(count.values()))