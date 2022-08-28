# 부분 문자열이 포함된 최소 윈도우
# 문자열 S와 T를 입력받아 O(n)에 T의 모든 문자가 포함된 S의 최소 윈도우를 찾아라
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 필요한 문자 각각의 수
        need = Counter(t)
        # 필요한 문자의 전체 수
        total = len(t)
        # 투 포인터
        left = 0
        # 결과
        answer = ''

        for right, c in enumerate(s, 1):
            # 현재 문자가 필요한 문자에 포함된다면 카운트
            if need[c] > 0:
                total -= 1
            need[c] -= 1
            # 필요한 문자를 모두 찾았다면
            if total == 0:
                # 왼쪽 포인터를 이동시킴
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                # 최소 크기의 윈도우 확인
                if not answer or right - left <= len(answer):
                    answer = s[left:right]
                    need[s[left]] += 1
                    left += 1
                    total += 1

        return answer



solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))
