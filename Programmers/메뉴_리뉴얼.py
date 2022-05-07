from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for c in course:
        check_menus = []
        for order in orders:
            for comb in list(combinations(order, c)):
                check_menus.append(''.join(sorted(comb)))
        menu_list = Counter(check_menus).most_common()
        for x, y in menu_list:
            if y > 1 and y == menu_list[0][1]:
                answer.append(x)

    return sorted(answer)