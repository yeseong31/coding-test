# 강의실 배정
import heapq
import sys

input = sys.stdin.readline

n = int(input())
rooms = []
for _ in range(n):
    s, t = map(int, input().split())
    rooms.append((s, t))

rooms.sort()
end_time = []
heapq.heappush(end_time, rooms[0][1])

answer = 0
for i in range(n - 1):
    # 현재 회의의 끝나는 시간이 다음 회의가 빨리 시작한다면
    if end_time[0] > rooms[i + 1][0]:
        heapq.heappush(end_time, rooms[i + 1][1])
    else:
        heapq.heappop(end_time)
        heapq.heappush(end_time, rooms[i + 1][1])

print(len(end_time))
