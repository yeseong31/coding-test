def solution(num):
    def collatz(n, cnt):
        if cnt == 500:
            return -1
        if n == 1:
            return cnt
        if n % 2 == 0:
            return collatz(n // 2, cnt + 1)
        else:
            return collatz(3 * n + 1, cnt + 1)
    
    return collatz(num, 0)
