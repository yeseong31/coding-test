import collections
import math


def solution(fees, records):
    answer = []

    dic = collections.defaultdict(list)
    for record in records:
        t, car_num, log = record.split()
        t = int(t[:2]) * 60 + int(t[3:])
        dic[car_num].append(t)

    for k in dic:
        # 23:59 출차 처리
        if len(dic[k]) % 2 == 1:
            dic[k].append(23 * 60 + 59)
        # 누적 주차 시간 계산
        parking_time = 0
        while dic[k]:
            end, start = dic[k].pop(), dic[k].pop()
            parking_time += end - start
        # 주차 시간이 '기본 시간'을 초과하면 '단위 시간'마다 '단위 요금'을 청구함
        total_charge = fees[1]
        if parking_time > fees[0]:
            total_charge += math.ceil(float(parking_time - fees[0]) / float(fees[2])) * fees[3]
        answer.append([total_charge, k])

    return list(zip(*sorted(answer, key=lambda x: x[1])))[0]


fees = [120, 0, 60, 591]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
print(solution(fees, records))
