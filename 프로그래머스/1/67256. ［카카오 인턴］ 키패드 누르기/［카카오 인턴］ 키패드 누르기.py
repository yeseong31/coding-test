def solution(numbers, hand):
    answer = []
    lx, ly, rx, ry = 3, 0, 3, 2
    dic = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2), 0: (3, 1)
    }
    
    for number in numbers:
        if number not in (2, 5, 8, 0):
            if number in (1, 4, 7):           
                answer.append('L')
                lx, ly = dic[number]
            else:
                answer.append('R')
                rx, ry = dic[number]
            continue

        ld = abs(lx - dic[number][0]) + abs(ly - dic[number][1])
        rd = abs(rx - dic[number][0]) + abs(ry - dic[number][1])
        if ld == rd:
            if hand == 'right':
                answer.append('R')
                rx, ry = dic[number]
            else:
                answer.append('L')
                lx, ly = dic[number]
        elif ld < rd:
            answer.append('L')
            lx, ly = dic[number]
        else:
            answer.append('R')
            rx, ry = dic[number]
        
    return ''.join(answer)