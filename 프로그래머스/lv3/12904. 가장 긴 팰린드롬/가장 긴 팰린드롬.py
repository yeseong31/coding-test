def even_palindrome(s, left, right):
    result = 0
    i = 0
    
    while 0 <= left - i and right + i < len(s) and s[left - i] == s[right + i]:
        i += 1
        result += 2
    
    return result


def odd_palindrome(s, mid):
    result = 1
    i = 1
    
    while 0 <= mid - i and mid + i < len(s) and s[mid - i] == s[mid + i]:
        i += 1
        result += 2
    
    return result


def solution(s):
    answer = 1

    for i in range(len(s)):
        answer = max(answer, odd_palindrome(s, i), even_palindrome(s, i - 1, i))

    return answer