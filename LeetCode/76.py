# Minimum Window Substring
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 결괏값
        answer = ''
        # 투 포인터
        left = 0
        # 필요한 문자 각각의 수
        needs = Counter(t)
        # 필요한 문자 전체 수
        total = len(t)

        for right, v in enumerate(s, 1):
            # 현재 문자가 '필요한 문자'라면
            if needs[v] > 0:
                total -= 1
            needs[v] -= 1
            # 필요한 문자를 모두 찾았다면
            if total == 0:
                # 왼쪽 포인터를 이동시킴
                while left < right and needs[s[left]] < 0:
                    needs[s[left]] += 1
                    left += 1
                # 최소 윈도우 판별
                if not answer or right - left <= len(answer):
                    answer = s[left:right]
                    needs[s[left]] += 1
                    left += 1
                    total += 1

        return answer
