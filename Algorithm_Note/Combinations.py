# 전체 수 n을 입력받아 k개의 조합을 리턴하라

def combine(n: int, k: int) -> list[list[int]]:
    result = []

    def dfs(elements, start: int, k: int):
        if k == 0:
            result.append(elements[:])
        
        # 자신 이전의 모든 값을 고정하여 재귀 호출 시행
        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([], 1, k)
    return result

# k개의 조합만을 생성해야 한다는 제약 조건이 추가된 문제이므로
# 전체 조합을 구하는 문제와는 조금 다른 유형이라는 점을 알아야 함

# 순열의 경우 자신을 제외하고 모든 요소를 next_elements로 처리했지만
# 조합의 경우 자기 자신을 포함하고, 앞의 모든 요소를 배제하고 next_elements를 구성함

# 파이썬의 itertools.combinations를 사용하면 더 쉽게 풀 수 있음

# [객체 복사]
# (1) [:]
# (2) copy() 메서드
# (3) copy.deepcopy() 메서드
