# 진법, 미리 구할 숫자의 개수, 게임 참가 인원, 튜브의 순서
def solution(n, t, m, p):
    def change(x):
        ans = []
        while x > 0:
            ans.append(x % n)
            x //= n
        return ans[::-1]

    answer = ''

    # 0부터 t - 1까지의 숫자를 미리 진법변환하여 저장해야 함
    lst = [0]
    for i in range(1, t * m):
        # 진법 변환한 숫자
        lst += change(i)

    for i in range(t):
        target = lst[p - 1]
        if target >= 10:
            target = ['A', 'B', 'C', 'D', 'E', 'F'][target - 10]
        answer += str(target)
        p += m

    return answer


print(solution(16, 16, 2, 2))
