# 에라토스테네스의 체

# 알고리즘
# 1) 2부터 N까지의 모든 자연수를 나열한다.
# 2) 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
# 3) 남은 수 중에서 i의 배수를 모두 제거한다... i는 제거하지 않고, N의 제곱근까지만 증가시켜 확인
# 4) 더 이상 반복할 수 없을 때까지 위의 과정을 반복한다.

import math


# 에라토스테네스의 체 알고리즘
def sieve_of_eratosthenes(n, array):
    for i in range(2, int(math.sqrt(n)) + 1):
        # i가 소수인 경우 i를 제외한 i의 모든 배수를 지우기
        if array[i]:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1


n = 10000
array = [True for _ in range(n + 1)]    # 처음엔 모든 수가 소수인 것으로 초기화

sieve_of_eratosthenes(n, array)
# 모든 소수 출력
for i in range(2, n + 1):
    if array[i]:
        print(i, end=' ')
