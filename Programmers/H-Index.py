def solution(citations):
    citations.sort()  # 오름차순 정렬
    n = len(citations)

    # h번 이상 인용된 논문이 h개 이상, 나머지 논문이 h개 이하일 때 h의 최댓값
    for h in range(n):
        if citations[h] >= n - h:
            return n - h
    return 0