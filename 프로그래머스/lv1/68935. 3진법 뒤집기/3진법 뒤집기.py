def solution(n):
    def change(x):
        result = []
        
        while x:
            x, mod = divmod(x, 3)
            result.append(str(mod))
        
        return ''.join(result)
    
    return int(change(n), 3)
