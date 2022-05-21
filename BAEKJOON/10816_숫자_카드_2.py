import sys
from collections import Counter

input = sys.stdin.readline

m = int(input())
cards = Counter(input().split())

x = int(input())
targets = [cards[i] for i in input().split()]
print(' '.join(map(str, targets)))
