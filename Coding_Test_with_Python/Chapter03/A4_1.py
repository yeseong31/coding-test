
# 단순하게 푸는 답안 예시

n, k = map(int, input().split())
result = 0

# N의 K 이상이라면 K로 계속 나누기
while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)
