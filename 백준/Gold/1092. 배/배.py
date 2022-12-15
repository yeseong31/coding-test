import sys
input = sys.stdin.readline


def solution():
    n = int(input())
    cranes = sorted(list(map(int, input().split())), reverse=True)
    m = int(input())
    boxes = sorted(list(map(int, input().split())), reverse=True)
    
    if cranes[0] < boxes[0]:
        return -1
    
    answer = 0
    while boxes:
        for c in range(n):
            if not boxes or cranes[c] < boxes[-1]:
                break
            for b in range(len(boxes)):
                if cranes[c] >= boxes[b]:
                    boxes.pop(b)
                    break
        answer += 1
    return answer


print(solution())
