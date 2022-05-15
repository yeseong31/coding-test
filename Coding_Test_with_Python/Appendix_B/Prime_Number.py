# 소수의 판별
import math


def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):       # 제곱근까지만 확인하여 시간 복잡도 개선... O(X) -> O(X^(1/2))
        if i % x == 0:
            return False
    return True


print(is_prime_number(4))
print(is_prime_number(7))
