# [N X M 크기의 2차원 리스트 초기화]
# - 2차원 리스트의 초기화는 반드시 '리스트 컴프리헨션'을 이용해야 함

n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)