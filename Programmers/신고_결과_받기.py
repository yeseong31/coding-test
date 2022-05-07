from collections import defaultdict


def solution(id_list, report, k):
    result = [0] * (len(id_list))

    report_users = defaultdict(list)

    for r in report:
        a, b = r.split()
        if a not in report_users[b]:
            report_users[b].append(a)

    for target in report_users:
        if len(report_users[target]) >= k:
            for user in report_users[target]:
                result[id_list.index(user)] += 1

    return result