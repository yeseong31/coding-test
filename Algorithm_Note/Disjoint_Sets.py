# 서로소 집합
# 공통 원소가 없는 두 집합

# 서로소 집합 자료구조의 연산 2가지
# union 연산은 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
# find 연산은 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산

# 알고리즘
# 1) union 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인
#     (i)  A와 B의 루트 노드 A', B'를 각각 찾음
#     (ii) A'를 B'의 부모 노드로 설정
# 2) 모든 union 연산을 처리할 때까지 위의 과정을 반복

# 이 알고리즘에서 유의할 점은 union 연산을 효과적으로 수행하기 위해 '부모 테이블' 정보를 항상 가지고 있어야 한다.
# 또한 루트 노드를 즉시 계산할 수 없고, 부모 테이블을 계속해서 확인하며 거슬러 올라가야 한다.

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


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

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')
print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')

# --------------------------------------------------------------------------------
# 위처럼 구현하면 find 함수가 모든 노드를 다 확인하기 때문에 시간 복잡도가 O(V)로 비효율적임.
# 현재의 알고리즘을 그대로 이용하면 전체 시간 복잡도는 O(VM)이 되어 굉장히 비효율적임.
# 이는 '경로 압축' 기법을 이용하여 개선할 수 있음.
