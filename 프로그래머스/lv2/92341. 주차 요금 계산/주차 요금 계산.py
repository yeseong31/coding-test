from math import ceil
from collections import defaultdict


def solution(fees, records):
    answer = []
    dt, df, ut, tf = fees
    in_time, total_time = defaultdict(int), defaultdict(int)

    for record in records:
        t, c, s = record.split()
        h, m = map(int, t.split(':'))
        if s == 'IN':
            in_time[c] = h * 60 + m
        else:
            total_time[c] += h * 60 + m - in_time[c]
            del in_time[c]

    for c in in_time:
        total_time[c] += 23 * 60 + 59 - in_time[c]

    for key in sorted(total_time.keys()):
        result = df
        if dt < total_time[key]:
            result += ceil((total_time[key] - dt) / ut) * tf
        answer.append(result)
        
    return answer