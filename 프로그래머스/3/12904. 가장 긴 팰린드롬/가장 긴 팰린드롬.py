def palindrome(s, left, right):
    result = i = not right - left
    
    while 0 <= left - i and right + i < len(s) and s[left - i] == s[right + i]:
        i += 1
        result += 2
    
    return result


def solution(s):
    answer = 1
    
    for i in range(len(s)):
        answer = max(answer, palindrome(s, i, i), palindrome(s, i - 1, i))
    
    return answer
