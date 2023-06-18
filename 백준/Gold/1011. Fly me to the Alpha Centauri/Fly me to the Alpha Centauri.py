t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    d = y - x
    c = 0
    c_move = 1
    c_move_plus = 0
    while c_move_plus < d:
        c += 1
        c_move_plus += c_move
        if c % 2 == 0:
            c_move += 1
    print(c)