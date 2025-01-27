import sys

def draw_star(i, j):
    while i != 0:
        if i % 3 == 1 and j % 3 == 1:
            sys.stdout.write(' ')
            return None
        i //= 3
        j //= 3
    sys.stdout.write('*')

n = int(input())
for i in range(n):
    for j in range(n):
        draw_star(i, j)
    sys.stdout.write('\n')