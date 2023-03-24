import heapq


def solution(program):
    answer = [0] * 10
    q, t = [], 0
    program.sort(key=lambda x: (x[1], x[0]), reverse=True)
    
    while q or program:
        if program and program[-1][1] <= t:
            heapq.heappush(q, (program.pop()))
        if not q:
            t += 1
            continue

        a, b, c = heapq.heappop(q)
        answer[a - 1] += t - b
    
        while program and t <= program[-1][1] <= t + c:
            heapq.heappush(q, (program.pop()))
        t += c

    return [t] + answer
