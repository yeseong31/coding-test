# Largest Merge Of Two Strings
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        i = j = 0
        answer = ''

        while i < n and j < m:
            if word1[i] > word2[j]:
                answer += word1[i]
                i += 1
            elif word1[i] < word2[j]:
                answer += word2[j]
                j += 1
            else:
                if word1[i:] > word2[j:]:
                    answer += word1[i]
                    i += 1
                else:
                    answer += word2[j]
                    j += 1

        return answer + word1[i:] + word2[j:]
