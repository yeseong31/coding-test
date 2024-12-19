for _ in range(int(input())):
    # 동전의 가지 수
    n = int(input())
    # 동전의 각 금액
    money = list(map(int, input().split()))
    # 만들어야 할 금액
    target = int(input())

    # DP 테이블
    dp = [0] * (target + 1)
    dp[0] = 1
    
    for m in money:
        for i in range(target + 1):
            if i >= m:
                dp[i] += dp[i - m]

    print(dp[target])