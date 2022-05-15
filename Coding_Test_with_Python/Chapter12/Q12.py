"""
기둥과 보 설치 (329p)
"""


def solution(n, build_frame):
    def check(res):
        for x, y, a in res:
            # 기둥: 바닥 위에 있거나, 보의 한쪽 끝 부분 위에 있거나, 다른 기둥 위에 있거나
            if a == 0:
                if y == 0 or [x - 1, y, 1] in res or [x, y, 1] in res or [x, y - 1, 0] in res:
                    continue
                return False
            # 보: 한쪽 끝 부분이 기둥 위에 있거나, 양쪽 끝 부분이 다른 보와 동시에 연결되어 있거나
            elif a == 1:
                if [x, y - 1, 0] in res or [x + 1, y - 1, 0] in res or \
                        ([x - 1, y, 1] in res and [x + 1, y, 1] in res):
                    continue
                return False
        return True

    result = []
    # x, y: 좌표
    # a: 0은 기둥, 1은 보
    # b: 0은 삭제, 1은 설치
    for frame in build_frame:
        x, y, a, b = frame
        # 삭제
        if b == 0:
            # 삭제가 가능한 구조물인가?
            result.remove([x, y, a])
            # 삭제가 불가능한 경우 다시 추가
            if not check(result):
                result.append([x, y, a])
        # 설치
        elif b == 1:
            # 설치가 가능한 구조물인가?
            result.append([x, y, a])
            # 설치가 불가능한 경우 다시 삭제
            if not check(result):
                result.remove([x, y, a])

    return sorted(result)



n = 5
build_frame = 	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n, build_frame))