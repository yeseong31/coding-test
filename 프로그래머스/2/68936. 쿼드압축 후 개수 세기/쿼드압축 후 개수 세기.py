def solution(arr):
    def calculate(a, b, c, d):
        zero = one = 0
        for z, o in a, b, c, d:
            zero += z
            one += o
        return zero, one
    
    def dfs(x, y, size):
        w = size // 2
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != arr[x][y]:
                    return calculate(dfs(x, y, w), dfs(x + w, y, w), dfs(x, y + w, w) , dfs(x + w, y + w, w))
                
        if arr[x][y] == 0:
            return 1, 0
        return 0, 1
        
    return dfs(0, 0, len(arr))