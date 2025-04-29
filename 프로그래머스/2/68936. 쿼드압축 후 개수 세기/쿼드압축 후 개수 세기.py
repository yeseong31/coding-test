def solution(arr):
    answer = [0, 0]
    separate(arr, 0, 0, len(arr), answer)
    return answer


def separate(arr, x, y, n, answer):
    value = arr[x][y]
    k = n // 2
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != value:
                separate(arr, x, y, k, answer)
                separate(arr, x, y + k, k, answer)
                separate(arr, x + k, y, k, answer)
                separate(arr, x + k, y + k, k, answer)
                return
    
    answer[value] += 1
