from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = set()
        n1, n2 = sorted(nums1), sorted(nums2)
        i = j = 0
        while i < len(n1) and j < len(n2):
            if n1[i] == n2[j]:
                answer.add(n1[i])
                i += 1
                j += 1
            elif n1[i] < n2[j]:
                i += 1
            else:
                j += 1
        return answer