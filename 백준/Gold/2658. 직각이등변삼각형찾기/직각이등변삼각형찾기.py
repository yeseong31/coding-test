def solution():
    def check(arr):
        if len(arr) < 2 or len(arr) > 10:
            return False

        length = [len(x) for x in arr]
        if length[0] == length[-1]:
            l, r = 0, len(length) - 1
            c = 1
            while l < r:
                if not length[l] == length[r] == c:
                    return False
                l += 1
                r -= 1
                c += 1
            if l == r and length[l] == length[r] == c:
                return True
            return False

        length.sort()
        if length == list(range(1, length[-1] + 1, 1)) or length == list(range(1, length[-1] + 1, 2)):
            return True
        return False

    target = []
    for i in range(10):
        tmp = []
        for j, k in enumerate(input()):
            if k == '1':
                tmp.append((i, j))
        if tmp:
            target.append(tmp)

    if not check(target):
        print(0)
        return

    p = sorted(target, key=lambda x: len(x), reverse=True)
    answer = [p.pop()[0]]

    if len(p[-1]) == 1:
        answer.append(p.pop()[0])
        if answer[0][1] == p[0][0][1]:
            answer.append(p[0][-1])
        else:
            answer.append(p[0][0])
    else:
        answer.append(p[0][0])
        answer.append(p[0][-1])

    for a, b in sorted(answer):
        print(a + 1, b + 1)
    return


solution()