# 집의 수
n = int(input())
# 집의 위치
home = list(map(int, input().split()))

print(sorted(home)[(n - 1) // 2])