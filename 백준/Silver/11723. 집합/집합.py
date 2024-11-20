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