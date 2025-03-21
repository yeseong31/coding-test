def get_box_counts(w, box, floor):
    left = box - (w * floor)
    right = w * (floor + 1) - (box + 1)
    
    if floor % 2 == 1:
        left, right = right, left
        
    return left, right

def get_next_box(box, left, right, floor):
    if floor % 2 == 0:
        return box + (2 * right + 1)
    else:
        return box + (2 * left + 1)


def solution(n, w, num):
    answer = 1
    n, box = n - 1, num - 1
    
    floor = box // w
    left, right = get_box_counts(w, box, floor)
    
    while True:
        next_box = get_next_box(box, left, right, floor)
        if next_box > n:
            break
        
        box = next_box
        answer += 1
        floor += 1
        
    return answer