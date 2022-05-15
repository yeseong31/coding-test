import heapq

n = int(input())
numbers = [int(input()) for _ in range(n)]
heapq.heapify(numbers)
print(numbers)
