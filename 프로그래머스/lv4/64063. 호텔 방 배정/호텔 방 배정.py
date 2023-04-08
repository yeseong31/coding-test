import sys
from collections import defaultdict

sys.setrecursionlimit(2000)


def find_empty_room(n, rooms):
    if not rooms[n]:
        rooms[n] = n + 1
        return n
    next_n = find_empty_room(rooms[n], rooms)
    rooms[n] = next_n + 1
    return next_n


def solution(k, room_number):
    answer = []
    rooms = defaultdict(int)
    for n in room_number:
        check_in = find_empty_room(n, rooms)
    return list(rooms)
