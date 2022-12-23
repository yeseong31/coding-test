from itertools import permutations


def solution(n, weak, dist):
    answer = len(dist) + 1
    length = len(weak)
    # 취약 지점을 일렬로 풀어냄
    weak += [x + n for x in weak]
    # 친구 순열 생성
    friends = list(permutations(dist, len(dist)))
    # weak 길이만큼 반복하여 확인
    for i in range(length):
        # 시작 지점부터 친구를 하나씩 추가
        for friend in friends:
            cnt = 1        
            # 현재 투입 인원이 확인 가능한 범위
            check = weak[i] + friend[cnt - 1]
            # weak 내 원소를 출발점으로 하여 취약 지점 확인
            for j in range(i, i + length):
                # 친구를 투입하여 취약 지점 확인
                if check < weak[j]:
                    cnt += 1
                    # 투입할 친구가 없다면 취약 지점을 전부 다 확인하지 못한 것이므로 break
                    if cnt > len(dist):
                        break
                    check = weak[j] + friend[cnt - 1]
            # 친구를 적게 투입하는 경우를 저장
            answer = min(answer, cnt)
            
    return answer if answer <= len(dist) else -1