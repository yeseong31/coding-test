# 흙길 보수하기
import math
import sys
input = sys.stdin.readline

answer = p = 0
n, l = map(int, input().split())
for s, e in sorted([[int(x) for x in input().split()] for _ in range(n)]):
    s = max(s, p)
    d = math.ceil((e - s) / l)
    answer += d
    p = s + d * l
print(answer)

# 111222..333444555.... // 길이 3인 널빤지
# .MMMMM..MMMM.MMMM.... // 웅덩이
# 012345678901234567890 // 좌표
