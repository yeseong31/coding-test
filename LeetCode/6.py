# Zigzag Conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        seq = -1
        i = j = 0
        result = [[] for _ in range(numRows)]

        while i < len(s):
            result[j].append(s[i])
            if j == 0 or j == numRows - 1:
                seq *= -1
            j += seq
            i += 1

        answer = ''
        for r in result:
            answer += ''.join(r)
        return answer
