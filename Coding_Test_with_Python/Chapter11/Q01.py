# 모험가 길드(311p)

n = int(input())
data = list(map(int, input().split()))

# 공포도가 X인 모험가는 반드시 X명 이상으로 구성해야 함
# 단, 몇 명의 모험가는 마을에 그대로 남아 있어도 됨
# 여행을 떠날 수 있는 그룹 수의 최댓값은?

data.sort(reverse=True)

idx = 0
count = 0
while idx < n:
    d = data[idx:idx+data[idx]]
    if len(d) >= max(d):
        count += 1
    idx += len(d)

print(count)
