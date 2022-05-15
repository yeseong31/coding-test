# 크루스칼 알고리즘
# 대표적인 최소 신장 트리 알고리즘
# 신장 트리 중에서 최소 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘
# 그리디 알고리즘으로 분류

# 신장 트리
# 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
# 이때 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 트리의 성립 조건이기도 함.

# 알고리즘
# 1) 간선 데이터를 비용에 따라 오름차순으로 정렬
# 2) 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
#     (i)  사이클이 발생하지 않는 경우 최소 신장 트리에 포함
#     (ii) 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않음
# 3) 모든 간선에 대해 위의 과정을 반복

# 최종적으로 신장 트리에 포함되는 간선의 개수가 '노드의 개수 - 1'

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

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

# 입력 예시
# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25
# 출력 예시
# 159

# 시간 복잡도 O(ElogE)... 간선 정렬이 가장 오래 걸림
