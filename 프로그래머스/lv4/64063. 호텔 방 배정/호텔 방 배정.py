import sys
sys.setrecursionlimit(2000)

def solution(k, room_number):
    def find_empty_room(check: int, rooms: dict):
        if check not in rooms:
            rooms[check] = check + 1
            return check
        empty_room = find_empty_room(rooms[check], rooms)
        rooms[check] = empty_room + 1
        return empty_room
    
    rooms = dict()
    return [find_empty_room(x, rooms) for x in room_number]