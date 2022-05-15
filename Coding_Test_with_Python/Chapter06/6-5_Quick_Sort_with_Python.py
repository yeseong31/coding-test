# 파이썬의 장점을 살린 퀵 정렬
# 평균 O(NlogN)
# 최악의 경우 O(N^2)... (데이터가 이미 정렬되어 있는 경우)

def quick_sort_py(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    # 피벗과 피벗을 제외한 리스트
    pivot = array[0]
    tail = array[1:]
    # 피벗을 기준으로 왼쪽/오른쪽 분할
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if pivot < x]
    # 분할 이후 왼쪽/오른쪽 부분에서 각각 정렬 수행 후, 전체 리스트 반환
    return quick_sort_py(left_side) + [pivot] + quick_sort_py(right_side)


a = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(quick_sort_py(a))
