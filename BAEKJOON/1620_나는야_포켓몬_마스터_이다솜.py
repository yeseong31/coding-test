import sys
input = sys.stdin.readline

# 포켓몬의 개수 n, 맞춰야 하는 문제의 수 m
n, m = map(int, input().split())
# 1번부터 n번까지의 포켓몬
pokemons = {}
for i in range(1, n + 1):
    target = input().strip()
    pokemons[target] = i
    pokemons[i] = target

for _ in range(m):
    s = input().strip()
    if s.isdigit():
        print(pokemons[int(s)])
    else:
        print(pokemons[s])
