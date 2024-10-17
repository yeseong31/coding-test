import sys
input = sys.stdin.readline

n = int(input())
cards = set(map(int, input().split()))
m = int(input())

for target in list(map(int, input().split())):
    if target not in cards:
        print(0, end=' ')
    else:
        print(1, end=' ')