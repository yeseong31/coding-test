def cond(s, i, left, right):
    return (0 <= left - i) and (right + i < len(s)) and (s[left - i] == s[right + i])


def palindrome(s, left, right):
    result = i = not right - left
    
    while cond(s, i, left, right):
        i += 1
        result += 2
    
    return result


def solution(s):
    answer = 1
    
    for i, _ in enumerate(s):
        answer = max(answer, palindrome(s, i, i), palindrome(s, i - 1, i))
    
    return answer
