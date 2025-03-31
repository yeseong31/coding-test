import collections
import sys
input = sys.stdin.readline

n = int(input())
data = []
sum_value = 0

for _ in range(n):
    v = int(input())
    data.append(v)
    sum_value += v

data.sort()

print(round(sum_value / n))   # 산술평균

# 중앙값
print(data[len(data) // 2])

# 최빈값... 여러 개 있으면 최빈값 중 두 번째로 작은 값 출력
cnt = collections.Counter(data).most_common()

if n > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

print(data[-1] - data[0])   # 범위