import sys


data = []
input = sys.stdin.readline
for _ in range(int(input())):
    data.append(int(input()))
for d in sorted(data):
    print(d)