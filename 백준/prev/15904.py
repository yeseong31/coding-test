# UCPC는 무엇의 약자일까?

check = ''
for word in input().split():
    for i, c in enumerate(word):
        if c.isupper():
            check += c

answer = 'I hate UCPC'
ucpc = 'UCPC'
i = 0
for c in check:
    if c == ucpc[i]:
        i += 1
    if i == 4:
        answer = 'I love UCPC'
        break

print(answer)
