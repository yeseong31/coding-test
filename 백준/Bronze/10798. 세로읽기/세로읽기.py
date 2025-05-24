from itertools import zip_longest

answer = []
words = [list(input()) for _ in range(5)]

for x in zip_longest(*words, fillvalue=''):
    answer.extend(x)

print(''.join(answer))