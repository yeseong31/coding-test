import sys
sys.setrecursionlimit(2000)


def solution(k, room_number):
    def find_empty_room(n: int, rooms: dict):
        if n not in rooms:
            rooms[n] = n + 1
            return n
        
        rooms[n] = find_empty_room(rooms[n], rooms) + 1
        return rooms[n] - 1
    
    rooms = dict()
    return [find_empty_room(x, rooms) for x in room_number]
