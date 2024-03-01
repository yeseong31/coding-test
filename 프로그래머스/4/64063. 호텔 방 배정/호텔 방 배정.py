import sys
sys.setrecursionlimit(2000)


def dfs(number, rooms):
    if number not in rooms:
        rooms[number] = number + 1
        return number

    room = dfs(rooms[number], rooms)
    rooms[number] = room + 1
    return room


def solution(k, room_number):
    rooms = dict()
    
    for number in room_number:
        dfs(number, rooms)
    
    return list(rooms)