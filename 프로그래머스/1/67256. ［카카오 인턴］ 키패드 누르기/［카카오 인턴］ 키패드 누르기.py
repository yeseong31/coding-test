from math import sqrt


class Point:
    def __init__(self, x, y):
        self.keypad = {
            1: (0, 0), 2: (0, 1), 3: (0, 2),
            4: (1, 0), 5: (1, 1), 6: (1, 2),
            7: (2, 0), 8: (2, 1), 9: (2, 2),
            0: (3, 1),
        }
        self.x = x
        self.y = y
    
    def move_to(self, number):
        nx, ny = self.keypad[number]
        self.x = nx
        self.y = ny
        
    def get_distance(self, number):
        nx, ny = self.keypad[number]
        return abs(self.x - nx) + abs(self.y - ny)
        

def solution(numbers, hand):
    result = []
    left = Point(3, 0)
    right = Point(3, 2)
    
    for n in numbers:
        if n in (1, 4, 7):
            result.append('L')
            left.move_to(n)
            continue
            
        if n in (3, 6, 9):
            result.append('R')
            right.move_to(n)
            continue
            
        left_dist = left.get_distance(n)
        right_dist = right.get_distance(n)

        if left_dist == right_dist:
            if hand == 'right':
                result.append('R')
                right.move_to(n)
            else:
                result.append('L')
                left.move_to(n)
        elif left_dist < right_dist:
            result.append('L')
            left.move_to(n)
        else:
            result.append('R')
            right.move_to(n)
    
    return ''.join(result)