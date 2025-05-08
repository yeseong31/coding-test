from collections import defaultdict, Counter
from itertools import combinations


def solution(orders, course):
    answer = []
    counter = defaultdict(int)
    
    for order in orders:
        for c in course:
            for comb in combinations(order, c):
                counter[''.join(sorted(comb))] += 1
    
    menus = defaultdict(list)
    for name, count in counter.items():
        menus[len(name)].append((name, count))
    
    for menu_lst in menus.values():
        max_count = max(x[1] for x in menu_lst)
        for o, v in sorted(menu_lst, key=lambda x: x[1], reverse=True):
            if v != max_count or v == 1:
                break
            answer.append(o)
        
    return sorted(answer)