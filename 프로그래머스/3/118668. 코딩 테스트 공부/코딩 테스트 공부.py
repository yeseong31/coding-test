from heapq import heappush, heappop


def solution(alp, cop, problems):
    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]

    max_alp = max(problem[0] for problem in problems)
    max_cop = max(problem[1] for problem in problems)

    q = [(0, (alp, cop))]
    checked = {(alp, cop): 0}
    limit = 150

    while q[0][1][0] < max_alp or q[0][1][1] < max_cop:
        time, (alp, cop) = heappop(q)

        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if alp < alp_req or cop < cop_req:
                continue

            next_cost = time + cost
            next_alp = min(alp + alp_rwd, limit)
            next_cop = min(cop + cop_rwd, limit)

            if (next_alp, next_cop) in checked and checked[(next_alp, next_cop)] <= next_cost:
                continue
            
            checked[(next_alp, next_cop)] = next_cost
            heappush(q, (next_cost, (next_alp, next_cop)))

    return heappop(q)[0]
