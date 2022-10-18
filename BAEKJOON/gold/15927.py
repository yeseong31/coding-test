# 회문은 회문아니야!!
import sys
input = sys.stdin.readline


def solution(s):
    def check_palindrome(target, left, right):
        while left < right:
            if target[left] != target[right]:
                return False
            left += 1
            right -= 1
        return True

    n = len(s)
    if not check_palindrome(s, 0, n - 1):
        return n
    elif not check_palindrome(s, 0, n - 2):
        return n - 1
    return -1


print(solution(input().strip()))
