def permute(nums: list[int]) -> list[list[int]]:
    result, prev_elements = [], []

    def dfs(elements):
        # 리프 노드일 때 결과 추가
        if len(elements) == 0:
            result.append(prev_elements[:])

        # 순열 생성 재귀 호출
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return result

# 레벨이 증가할수록 자식 노드의 개수는 점점 작아짐

# 이전 값을 하나씩 덧붙여 계속 재귀 호출을 진행하다가 리프 노드에 도달한 경우,
# 즉 len(elements) == 0일 때 결과를 하나씩 담음
# 이때 중요한 부분은 결과를 추가할 때 prev_elements[:]로 처리하여
# 값을 복사하는 형태로 참조 관계를 갖지 않도록 처리해야 함

# 파이썬의 경우 'itertools.permutations'를 이용하면 훨씬 빠르게 처리할 수 있음
