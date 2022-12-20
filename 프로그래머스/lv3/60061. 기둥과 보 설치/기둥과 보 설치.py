def check(board):
    for x, y, a in board:
        # 기둥: 바닥 위에 있거나 보의 한쪽 끝부분 위에 있거나, 또는 다른 기둥 위에 있어야 함
        if a == 0 and (y == 0 or (x - 1, y , 1) in board or (x, y, 1) in board or (x, y - 1, 0) in board):
            continue
        # 보: 한쪽 끝부분이 기둥 위에 있거나, 또는 양쪽 끝부분이 다른 보와 동시에 연결되어 있어야 함
        elif a == 1 and ((x, y - 1, 0) in board or (x + 1, y - 1, 0) in board or ((x - 1, y, 1) in board and (x + 1, y, 1) in board)):
            continue
        return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 0:
            answer.remove((x, y, a))
            if not check(answer):
                answer.append((x, y, a))
        else:
            answer.append((x, y, a))
            if not check(answer):
                answer.remove((x, y, a))
    return sorted(answer)
