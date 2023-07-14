import sys
sys.setrecursionlimit(2000)


def solution(k, room_number):
    def reserve(n):
        if n not in rooms:
            rooms[n] = n + 1
            return n
        
        empty = reserve(rooms[n])
        rooms[n] = empty + 1
        return empty
        
    
    rooms = dict()
    return [reserve(i) for i in room_number]