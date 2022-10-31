import itertools

def solution(n, weak, dist):
    # 점검하기 위해 보내야 하는 친구 수의 최솟값
    answer = len(dist) + 1

    # 원형 데이터를 평평하게 만듦
    length = len(weak)
    for i in range(length):
        weak.append(n + weak[i])

    # 취약 지점의 길이만큼 시작 지점을 결정하여 탐색
    for start in range(length):
        # 투입할 수 있는 친구를 나열
        for friends in list(itertools.permutations(dist, len(dist))):
            # 친구 투입
            count = 1
            # 다음 위치 업데이트
            next_position = weak[start] + friends[count - 1]
            for idx in range(start, start + length):
                # 만약 다음 취약 지점까지 도달하지 못했다면, 친구 한 명을 더 투입
                if next_position < weak[idx]:
                    count += 1
                    # 만약 투입할 친구가 없다면, 그대로 종료
                    if count > len(dist):
                        break
                    # 다음 위치 업데이트
                    next_position = weak[idx] + friends[count - 1]
            answer = min(answer, count)

    if answer > len(dist):
        return -1
    return answer