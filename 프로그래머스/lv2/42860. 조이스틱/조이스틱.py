def solution(name):
    def to_A(i):
        return min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
    
    n = len(name)
    target = ['A'] * n
    count = sum(to_A(i) for i in range(n))
    min_step = n - 1
    
    for i, c in enumerate(name):
        x = i + 1
        while x < n and name[x] == 'A':
            x += 1
        min_step = min(min_step, 2 * i + (n - x), i + 2 * (n - x))
    
    return min_step + count