def solution(name):
    answer = 0
    min_step = len(name) - 1

    while min_step > 0 and name[min_step] == 'A':
        min_step -= 1

    if min_step < 0:
        return answer

    for i, c in enumerate(name):
        answer += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)

        next_i = i + 1
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1

        min_step = min(min_step, i + i + len(name) - next_i)

    answer += min_step
    return answer


'''
def solution(name):
    def set_char(c) -> int:
        alpha1, alpha2 = "ABCDEFGHIJKLM", "NOPQRSTUVWXYZ"
        if c in alpha1:
            return alpha1.index(c)
        return abs(alpha2.index(c) - 13)

    def find_shortest_a(i: int, t: list):
        left = right = i
        cl = cr = 1

        while cl < len(t):
            left = left - 1 if left > 0 else len(t) - 1
            if t[left] != 'A':
                break
            cl += 1

        while cr < len(t):
            right = right + 1 if right < len(t) - 1 else 0
            if t[right] != 'A':
                break
            cr += 1

        if cr <= cl:
            return [right, cr]
        return [left, cl]

    answer = 0
    idx = 0
    target = list(name)

    while True:
        answer += set_char(target[idx])
        target[idx] = 'A'
        if target.count('A') == len(name):
            break
        next_idx, step = find_shortest_a(idx, target)
        answer += step
        idx = next_idx

    return answer
'''


