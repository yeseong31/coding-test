import sys
sys.setrecursionlimit(2_000)


def find_empty_room(rooms, x):
    if x not in rooms:
        rooms[x] = x + 1
        return x
    
    empty_room = find_empty_room(rooms, rooms[x])
    rooms[x] = empty_room + 1
    return empty_room
    

def solution(k, room_number):
    rooms = dict()
    return [find_empty_room(rooms, x) for x in room_number]
