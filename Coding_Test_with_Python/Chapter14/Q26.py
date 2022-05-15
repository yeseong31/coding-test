"""
카드 정렬하기 (363p)
"""
import heapq

n = int(input())

# 우선순위 큐
# 제일 작은 숫자들을 묶어나가면 효율적인 방법
q = []
for number in range(n):
    heapq.heappush(q, int(input()))

result = 0

while len(q) > 1:
    first = heapq.heappop(q)
    second = heapq.heappop(q)
    sum_value = first + second
    result += sum_value
    heapq.heappush(q, sum_value)

print(result)
