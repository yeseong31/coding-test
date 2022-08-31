import collections


def check(q, value):
    for v, i in q:
        if v > value:
            return True
    return False


def solution(n: int, m: int, docs: list[int]) -> int:
    if n == 1:
        return 1

    q = collections.deque()
    for i, d in enumerate(docs):
        q.append((d, i))

    cnt = 1
    while q:
        # 현재 큐의 가장 앞 문서의 중요도 확인
        v, i = q.popleft()
        # 현재 문서보다 중요도가 높은 문서가 있다면
        if check(q, v):
            q.append((v, i))
        # 타겟 원소라면 출력 순서 반환
        elif i == m:
            return cnt
        # 그렇지 않으면 출력 순서 +1
        else:
            cnt += 1


for _ in range(int(input())):
    # 문서의 개수 n, 타겟 m
    n, m = map(int, input().split())
    # 문서의 중요도
    documents = list(map(int, input().split()))
    # 결괏값 계산
    print(solution(n, m, documents))
