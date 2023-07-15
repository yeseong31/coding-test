from itertools import combinations
from collections import defaultdict
from bisect import bisect_left


def solution(info, query):
    answer = []
    applicant = defaultdict(list)
    
    # 지원자 정보
    for target in info:
        *q, score = target.split()
        # 주어진 정보를 키로 설정, 점수 추가
        applicant[''.join(q)].append(int(score))
        # 가능한 16가지 조합에 대한 점수 추가
        for x in range(4):
            for comb in combinations(q, x):
                applicant[''.join(comb)].append(int(score))
        
    # 점수 정렬
    for k in applicant:
        applicant[k].sort()
    
    for q in query:
        # 쿼리와 점수 분리
        *q, score = q.split()
        # 쿼리 전처리
        q = ''.join(q).replace('-', '').replace(' ', '').replace('and', '')
        # score를 넘는 지원자 수 카운트
        count = len(applicant[q]) - bisect_left(applicant[q], int(score))
        answer.append(count)
    
    return answer