import bisect
import collections
import copy
import itertools


def solution(info, query):
    answer = []
    dic = collections.defaultdict(list)

    # info 조합 생성
    for inf in info:
        inf = inf.split()
        cond, score = inf[:-1], int(inf[-1])

        # 모든 조합(16가지)에 대한 내용을 dic에 저장
        for i in range(5):
            for c in list(itertools.combinations([0, 1, 2, 3], i)):
                tmp = copy.deepcopy(cond)
                for j in c:
                    tmp[j] = '-'
                dic[''.join(tmp)].append(score)

    # 이진 탐색을 위해 점수 리스트 정렬
    for v in dic.values():
        v.sort()

    # 조건 확인
    for q in query:
        q = q.replace('and', '')
        q = q.split()
        target, score = ''.join(q[:-1]), int(q[-1])
        cnt = 0

        if target in dic:
            score_list = dic[target]
            # 이진 탐색: 원하는 값 '이상'이 나오는 지점을 검색
            i = bisect.bisect_left(score_list, score)
            cnt = len(score_list) - i

        answer.append(cnt)

    return answer


'''
def solution(info, query):
    answer = []

    new_query = []
    for q in query:
        q = q.replace('and', '')
        q = q.replace('-', '')
        q = q.split()
        cond, score = q[:-1], int(q[-1])
        new_query.append((cond, score))

    new_info = []
    for inf in info:
        tmp = []
        for i in inf.split():
            if i.isdigit():
                new_info.append((tmp, int(i)))
            else:
                tmp.append(i)

    # 쿼리문 하나씩 비교
    for q, score_q in new_query:
        cnt = 0
        for i, score_i in new_info:
            if set(q).issubset(set(i)) and score_i >= score_q:
                cnt += 1
        answer.append(cnt)

    return answer
'''

info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]
print(solution(info, query))
