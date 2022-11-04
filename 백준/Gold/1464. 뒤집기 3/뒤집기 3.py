s = input()
length = len(s)

for i in range(length - 1):
    if s[i] > s[i + 1] and s[0] >= s[i + 1]:
        s = s[:i + 1][::-1] + s[i + 1:]
        if s[i] >= s[i + 1]:
            s = s[:i + 2][::-1] + s[i + 2:]

print(s)