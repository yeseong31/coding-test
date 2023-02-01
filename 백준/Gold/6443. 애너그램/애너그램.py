import sys
from collections import Counter

input = sys.stdin.readline


def solution():
    def backtracking(n):
        if n == len(word):
            print(''.join(stack))
            return
        for v in count:
            if count[v] > 0:
                count[v] -= 1
                stack.append(v)
                backtracking(n + 1)
                count[v] += 1
                stack.pop()
    
    for _ in range(int(input())):
        stack = []
        word = sorted(input().strip())
        count = Counter(word)
        backtracking(0)


solution()
