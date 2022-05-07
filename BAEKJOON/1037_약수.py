# 약수의 개수 n
n = int(input())
numbers = sorted(list(map(int, input().split())))
print(numbers[0] * numbers[-1])
