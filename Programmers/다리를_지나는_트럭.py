# 다리에 올라갈 수 있는 트럭 수 / 다리가 견딜 수 있는 무게 / 트럭 별 무게(대기 트럭)
def solution(bridge_length, weight, truck_weights):
    time = 0
    # 다리를 건너는 트럭(최대 bridge_length개)
    moving = [0] * bridge_length
    # 현재 다리에 가해지는 하중
    w = 0

    while True:
        # 종료 조건: 트럭이 모두 다리를 건넌 경우(대기 트럭, 다리를 건너는 트럭 모두 없는 상태)
        if len(truck_weights) == 0 and w == 0:
            break

        time += 1
        # 현재 다리를 건너는 중에 있는 트럭이 있으면 다리를 지났다고 처리
        if moving[0] != 0:
            w -= moving[0]
        moving.pop(0)

        # 트럭이 다리를 건널 수 없는 상황이라면 0을, 그렇지 않으면 이후 트럭의 무게를 now에 저장
        now = 0

        # 트럭이 다리를 건너도록 함
        if truck_weights:
            # 다리를 건너는 중의 트럭들과 다음에 건널 트럭의 무게가 기준을 초과하지 않는 경우
            if w + truck_weights[0] <= weight:
                # 이번 차례에 건너야 할 트럭을 선정
                now = truck_weights.pop(0)
                w += now

        moving.append(now)

    return time