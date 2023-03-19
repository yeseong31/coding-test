# 삽입 정렬
# 최선의 경우 O(N)... (가정: 데이터가 거의 정렬되어 있는 상태)
# 최악의 경우 O(N^2)
def insertion_sort(array):
    """
    삽입 정렬
    :param array:
    - 정렬하고자 하는 배열
    :return:
    - 정렬된 배열
    """
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break
    return array
    
    
def insertion_sort2(array):
    """
    삽입 정렬 - 현재 위치부터 필요한 부분까지만 뒤로 가면서 위치를 바꾸도록 부분적으로 최적화
    :param array:
    - 정렬하고자 하는 배열
    :return:
    - 정렬된 배열
    """
    for idx in range(1, len(array)):
        i = idx
        while i > 0 and array[i - 1] > array[i]:
            array[i - 1], array[i] = array[i], array[i - 1]
            i -= 1
    return array


a = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(f'result = {insertion_sort(a)}')
print(f'result = {insertion_sort2(a)}')
