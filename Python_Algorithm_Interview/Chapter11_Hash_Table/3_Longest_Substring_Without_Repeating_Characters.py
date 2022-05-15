# 중복 문자 없는 가장 긴 부분 문자열(303p)

def lengthOfLongestSubstring(s: str) -> int:
    # 등장한 문자 저장
    used = {}
    max_len = left = 0
    for idx, c in enumerate(s):
        if c in used:
            left = used[c] + 1
        else:
            max_len = max(max_len, idx - left + 1)
        used[c] = idx

    return max_len




s = "abcabcbb"
print(lengthOfLongestSubstring(s))

s = "pwwkew"
print(lengthOfLongestSubstring(s))

s = "tmmzuxt"
print(lengthOfLongestSubstring(s))
