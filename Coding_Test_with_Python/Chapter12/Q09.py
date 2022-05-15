# 문자열 압축(323p)

from collections import defaultdict


def solution(s):
    result = 1001
    for cut in range(1, len(s) // 2 + 1):
        prev, res = '', ''
        idx, cnt = 0, 1
        while idx <= len(s):
            c = s[idx:idx + cut]
            # 연달아 나오는 문자이면
            if prev == c:
                cnt += 1
            # 연달아 나오는 문자가 아니라면
            else:
                res += prev if cnt <= 1 else str(cnt) + prev
                cnt = 1
            prev = c
            idx += cut
        # 나머지 문자열 처리
        res += c + s[idx:]
        result = min(result, res, key=lambda x: len(x))

    return len(result)


s = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd"
]

for i in s:
    print(solution(i))
