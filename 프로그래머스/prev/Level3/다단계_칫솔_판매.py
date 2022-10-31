import collections
import math


def solution(enroll, referral, seller, amount):
    graph = collections.defaultdict(str)
    total = collections.defaultdict(int)

    for ref, enr in zip(referral, enroll):
        graph[enr] = ref

    for sel, amo in zip(seller, amount):
        amo *= 100
        while True:
            if amo == 0:
                break
            elif graph[sel]:
                child = math.ceil(amo * 0.9)
                total[sel] += child
                amo -= child
                sel = graph[sel]
            else:
                total[sel] += amo
                break

    return [total[e] for e in enroll]


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))
