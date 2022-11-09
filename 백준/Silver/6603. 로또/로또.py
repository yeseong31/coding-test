from itertools import combinations

while True:
    _input = list(map(int, input().split()))
    if _input[0] == 0:
        break
    for comb in list(combinations(_input[1:], 6)):
        print(*comb)
    print()