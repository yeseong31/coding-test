"""
유효한 애너그램(507p)
t가 s의 애너그램인지 판별하라
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


s = "anagram"
t = "nagaram"
sol = Solution()
print(sol.isAnagram(s, t))
