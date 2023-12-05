box = [list(map(int, input().split())) for _ in range(3)]


def ccw(p1, p2, p3):
    return p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - (p2[0] * p1[1] + p3[0] * p2[1] + p1[0] * p3[1])


answer = ccw(*box)

if answer > 0:
    print(1)
elif answer == 0:
    print(0)
else:
    print(-1)
