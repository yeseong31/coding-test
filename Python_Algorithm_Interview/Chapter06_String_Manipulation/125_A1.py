# 풀이 1 - 리스트로 변환


# 대소문자 여부 상관없이 영문자, 숫자만을 대상으로 하므로 '전처리' 필요
def isPalindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True
