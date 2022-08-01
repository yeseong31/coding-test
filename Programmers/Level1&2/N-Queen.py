def solution(n):
    def queens(x):
        ans = 0
        if x == n + 1:
            return 1
        for i in range(1, n + 1):
            a, b = x + i, n + x - i
            if not (col[i] or d1[a] or d2[b]):
                col[i] = d1[a] = d2[b] = True
                ans += queens(x + 1)
                col[i] = d1[a] = d2[b] = False
        return ans

    col, d1, d2 = [False] * (n + 1), [False] * (2 * n + 1), [False] * (2 * n + 1)
    return queens(1)


'''
answer = 0


def solution(n):
    def set_queen(x):
        global answer
        if x == n:
            answer += 1
            return
        for i in range(n):
            # 1행 x열에 대해 Queen 배치
            queens[x] = i
            # 0 ~ x열까지 확인
            for j in range(x):
                # 같은 행/열 및 대각선이 겹치면 불가능
                if queens[j] == queens[x] or abs(queens[j] - queens[x]) == abs(j - x):
                    break
            else:
                set_queen(x + 1)

    global answer
    queens = [0] * n
    set_queen(0)
    return answer
'''


print(solution(12))
