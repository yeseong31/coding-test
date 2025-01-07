n, k = map(int, input().split())

money_list = []
for _ in range(n):
    money_list.append(int(input()))

count = 0
for money in sorted(money_list, reverse=True):
    count += k // money
    k %= money

print(count)