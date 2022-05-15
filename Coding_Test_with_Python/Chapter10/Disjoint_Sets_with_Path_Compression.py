# '경로 압축' 기법을 적용하여 개선된 서로소 집합

# 서로소 집합은 무방향 그래프 내에서의 사이클 판별에 사용할 수 있다.
# 루트 노드가 서로 같다면 사이클이 발생한 것으로 간주하는 것을 이용한다.

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드 개수, 간선(union 연산) 개수
v, e = map(int, input().split())

# 부모 테이블 초기화
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

# 사이클 발생 여부
cycle = False

for _ in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 union 연산 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print('사이클이 발생함')
else:
    print('사이클이 발생하지 않음')
