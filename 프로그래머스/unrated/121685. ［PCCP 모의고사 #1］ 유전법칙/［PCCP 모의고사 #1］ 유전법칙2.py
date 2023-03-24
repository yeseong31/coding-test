# 부모가 'Rr'이면 자식은 child의 인덱스대로 결정
# 그렇지 않으면 자식은 부모를 따라감
def dfs(gen, x, child):
    if gen == 1:
        return 'Rr'
    parent = dfs(gen - 1, x // 4, child)
    if parent == 'Rr':
        return child[x % 4]
    return parent


def solution(queries):
    child = ('RR', 'Rr', 'Rr', 'rr')
    return [dfs(n, p - 1, child) for n, p in queries]
