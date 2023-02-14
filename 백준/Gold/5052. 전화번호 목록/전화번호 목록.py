import sys


for _ in range(int(input())):
    n = int(input())
    phones = sorted([sys.stdin.readline().rstrip() for _ in range(n)])
    check = True
    for i in range(n - 1):
        if phones[i] == phones[i + 1][:len(phones[i])]:
            check = False
            break
    if not check:
        print('NO')
    else:
        print('YES')