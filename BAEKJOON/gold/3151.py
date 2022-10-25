# 합이 0
import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
students = sorted(list(map(int, input().split())))
count = Counter(students)
length = len(students)

answer = 0
for i in range(length - 2):
    left, right = i + 1, length - 1
    while left < right:
        target = students[left] + students[right] + students[i]
        if target == 0:
            if students[left] == students[right]:
                answer += right - left
            else:
                answer += count[students[right]]
            left += 1
        elif target < 0:
            left += 1
        else:
            right -= 1

print(answer)
