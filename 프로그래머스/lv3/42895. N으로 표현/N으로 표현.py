def solution(N, number):
    answer = 0
    # 연산 결과 저장 (N은 최대 8번 사용)
    dp = [set() for _ in range(9)]
    
    # N 사용
    for i in range(1, 9):
        # 연산 결과에 N을 i번 반복한 숫자 저장
        v = dp[i]
        v.add(int(str(N) * i))
        
        # 연산 횟수 지정
        for j in range(1, i):
            # 연산을 수행할 열 선택
            for k in dp[j]:
                # 이전 연산 결과에서부터 사칙 연산 수행
                for l in dp[i - j]:
                    v.add(k + l)
                    v.add(k - l)
                    v.add(k * l)
                    if k != 0 and l != 0:
                        v.add(k // l)
                        
        # 연산 결과 내 결괏값이 있다면 return
        if number in v:
            return i
        
    return -1