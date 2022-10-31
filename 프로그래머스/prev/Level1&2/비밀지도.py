def solution(n, arr1, arr2):
    board = []
    for i in range(n):
        tmp = []
        n1 = bin(arr1[i])[2:].zfill(n)
        n2 = bin(arr2[i])[2:].zfill(n)
        for j in range(n):
            if n1[j] == '1' or n2[j] == '1':
                tmp.append('#')
            else:
                tmp.append(' ')
        board.append(''.join(tmp))
    return board


n = 6
arr1 = 	[46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
print(solution(n, arr1, arr2))
