# 회살의 수, 어피치가 맞힌 과녁
import collections


def solution(n, info):
    def bfs():
        res = []
        q = collections.deque([(0, [0 for _ in range(11)])])
        gap = 0
        while q:
            cnt, board = q.popleft()
            # 화살을 모두 쐈다면 어피치, 라이언의 점수를 계산
            if sum(board) == n:
                apeach = ryan = 0
                for i in range(11):
                    if info[i] == board[i] == 0:
                        continue
                    if info[i] >= board[i]:
                        apeach += 10 - i
                    else:
                        ryan += 10 - i
                # 라이언이 이긴 경우
                diff = ryan - apeach
                if diff > 0:
                    if gap > diff:
                        continue
                    elif gap < diff:
                        gap = diff
                        res.clear()
                    res.append(board)
            # 화살을 초과해서 쏜 경우
            elif sum(board) > n:
                continue
            # 화살을 덜 쏜 경우 '-1' 표시
            elif cnt == 10:
                tmp = board.copy()
                tmp[cnt] = n - sum(tmp)
                q.append((-1, tmp))
            # 화살 발사
            else:
                # 어피치보다 1발 더 많이 쏘기
                tmp = board.copy()
                tmp[cnt] = info[cnt] + 1
                q.append((cnt + 1, tmp))
                # 이기지 못한다면 아예 쏘지 않기
                tmp2 = board.copy()
                tmp2[cnt] = 0
                q.append((cnt + 1, tmp2))
        return res

    result = bfs()
    if not result:
        return [-1]
    elif len(result) == 1:
        return result[0]
    return result[-1]



n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
print(solution(n, info))

n = 1
info = [1,0,0,0,0,0,0,0,0,0,0]
print(solution(n, info))

n = 9
info = 	[0,0,1,2,0,1,1,1,1,1,1]
print(solution(n, info))

n = 10
info = [0,0,0,0,0,0,0,0,3,4,3]
print(solution(n, info))

# 개수를 넘겨서 맞히거나 아예 맞히지 않고 다른 점수를 먹는 것을 고려해야 함
