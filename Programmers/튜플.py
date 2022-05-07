from collections import Counter

def solution(s):
    nums = []
    check = ''
    for v in s:
        if v.isdigit():
            check += v
            continue
        if check and v in ['}', ',']:
            nums.append(int(check))
        check = ''

    return [x[0] for x in Counter(nums).most_common()]