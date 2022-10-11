import itertools

group_data = itertools.groupby(input())
for g, v in group_data:
    print(f'({len(list(v))}, {g})', end=' ')
