# 회문
import sys
input = sys.stdin.readline


def check(word: str) -> bool:
    return word == word[::-1]


def is_palindrome(word: str) -> int:
    left, right = 0, len(word) - 1
    if word == word[::-1]:
        return 0
    while left < right:
        if word[left] != word[right]:
            if left < right - 1:
                if check(word[:right] + word[right + 1:]):
                    return 1
            if left + 1 < right:
                if check(word[:left] + word[left + 1:]):
                    return 1
            return 2
        else:
            left += 1
            right -= 1


for _ in range(int(input())):
    print(is_palindrome(input().strip()))
