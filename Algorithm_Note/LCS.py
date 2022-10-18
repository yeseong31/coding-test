# LCS

# 1. Longest Common Substring (최장 공통 문자열) -----------------------------------------------------------------------
# 현재의 두 문자가 같을 때 '두 문자의 앞 글자까지 공통 문자열이 지속되었다면' 계속 공통 문자열

a, b = 'abcdef', 'gbcdfe'
n = len(a)
lcs = [[0] * (n + 1) for _ in range(n + 1)]

answer = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if a[i - 1] == b[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
            answer = max(answer, lcs[i][j])
print(answer)  # return 최장 공통 문자열의 길이

# 2. Longest Common Subsequence (최장 공통 부분 수열) ------------------------------------------------------------------
# 최장 공통 문자열과 다른 점은 '비교하는 두 문자가 다를 때'
# 부분 수열은 '연속된 값이 아니므로' 현재 문자를 비교하는 과정 이전의 최대 공통 부분 수열은 계속 유지됨

a, b = 'abcdef', 'gbcdfe'
n = len(a)
lcs = [[0] * (n + 1) for _ in range(n + 1)]

answer = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if a[i - 1] == b[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
print(lcs[n][n])  # return 최장 공통 부분 수열의 길이

# 2-1. Longest Common Subsequence (최장 공통 부분 수열) 찾기 -----------------------------------------------------------
# LCS 배열의 가장 마지막 값에서부터
#     lcs[i - 1][j]와 lcs[i][j - 1] 중 현재 값과 같은 값을 찾고
#         같은 값이 있다면 그 곳으로 이동,
#         없다면 result 배열에 해당 문자를 넣고 lcs[i - 1][j - 1] 위치로 이동
#     최종적으로 0으로 이동 시 종료, result 배열을 뒤집어서 반환

result = []
i = j = n
while lcs[i][j] != 0:
    if lcs[i - 1][j] == lcs[i][j]:
        i -= 1
    elif lcs[i][j - 1] == lcs[i][j]:
        j -= 1
    else:
        result.append(a[j - 1])
        i -= 1
        j -= 1
print(''.join(result[::-1]))
