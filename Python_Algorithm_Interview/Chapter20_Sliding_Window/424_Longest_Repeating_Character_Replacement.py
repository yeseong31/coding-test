# 대문자로 구성된 문자열 s가 주어졌을 때 k번만큼 변경으로 만들 수 있는,
# 연속으로 반복된 문자열의 가장 긴 길이를 출력하라.

# 오른쪽(최대)에서 왼쪽(최소) 위치를 뺀 다음,
# 윈도우 내 출현 빈도가 가장 높은 문자의 수를 뺀 값이 k와 같은 수 있는 수 중 최댓값

import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 가장 많이 등장하는 문자 확인
        def most_common_char_cnt():
            return cnt.most_common()[0][1]

        # 문자 수 카운트
        cnt = collections.Counter()
        # 투 포인터
        left = right = 0

        for right in range(1, len(s) + 1):
            cnt[s[right - 1]] += 1
            # k 초과 시 left 이동
            if right - left - most_common_char_cnt() > k:
                cnt[s[left]] -= 1
                left += 1

        # 윈도우 사이즈 반환
        return right - left


solution = Solution()

s = "AABABBA"
k = 1
print(solution.characterReplacement(s, k))
