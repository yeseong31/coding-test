# 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

import sys

m = int(sys.stdin.readline())
s = set()

for _ in range(m):
    temp = sys.stdin.readline().strip().split()

    if len(temp) == 1:
        if temp[0] == "all":
            s = set(range(1, 21))
        else:
            s = set()
    else:
        cmd, n = temp[0], temp[1]
        n = int(n)

        if cmd == "add":
            s.add(n)
        elif cmd == "remove":
            s.discard(n)
        elif cmd == "check":
            print(1 if n in s else 0)
        elif cmd == "toggle":
            if n in s:
                s.discard(n)
            else:
                s.add(n)

# s = 0b0
# m = int(sys.stdin.readline())
#
# for _ in range(m):
#     target = sys.stdin.readline().rstrip().split()
#     if target == 'all':
#         s = (1 << 21) - 1
#     elif target == 'empty':
#         s = 0
#     else:
#         cmd, n = target
#         n = int(n) - 1
#         if cmd == 'add':
#             s |= (1 << n)
#         elif cmd == 'remove':
#             s &= ~(1 << n)
#         elif cmd == 'toggle':
#             s ^= (1 << n)
#         elif cmd == 'check':
#             print(1 if s & (1 << n) == 1 else 0)
