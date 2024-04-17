import collections


def check(q, value, idx):
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
        v, i = q.popleft()
        if check(q, v, i):
            q.append((v, i))
        elif i == m:
            return cnt
        else:
            cnt += 1


for _ in range(int(input())):
    n, m = map(int, input().split())
    documents = list(map(int, input().split()))
    print(solution(n, m, documents))