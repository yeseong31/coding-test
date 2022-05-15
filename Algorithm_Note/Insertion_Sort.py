# 삽입 정렬
# 최선의 경우 O(N)... (가정: 데이터가 거의 정렬되어 있는 상태)
# 최악의 경우 O(N^2)

def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break


a = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(a)
