def solution(n):
    def hanoi(x, start, mid, end):
        if x == 1:
            answer.append([start, end])
            return
        hanoi(x - 1, start, end, mid)
        answer.append([start, end])
        hanoi(x - 1, mid, start, end)
    
    answer = []
    hanoi(n, 1, 2, 3)
    return answer
