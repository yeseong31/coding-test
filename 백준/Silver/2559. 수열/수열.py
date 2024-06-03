n, k = map(int, input().split())
temperature = list(map(int, input().split()))

max_temperature = sum(temperature[:k])

check = max_temperature
p = 0

for i in temperature[k:]:
    check -= temperature[p]
    check += i
    max_temperature = max(max_temperature, check)
    p += 1

print(max_temperature)