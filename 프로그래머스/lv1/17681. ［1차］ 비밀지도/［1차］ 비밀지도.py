def solution(n, arr1, arr2):
    def get_row(x, y):
        return bin(x | y)[2:].zfill(n).replace('1', '#').replace('0', ' ')
    
    return [get_row(a, b) for a, b in zip(arr1, arr2)]