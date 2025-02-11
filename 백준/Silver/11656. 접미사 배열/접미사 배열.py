s = input()
result, cur = [], ''
for i in range(len(s) - 1, -1, -1):
    cur += s[i]
    result.append(cur[::-1])
for res in sorted(result):
    print(res)