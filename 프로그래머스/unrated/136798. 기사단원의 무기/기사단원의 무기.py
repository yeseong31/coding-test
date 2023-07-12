def solution(number, limit, power):
    def count_gcd(n):
        count = 0
        for m in range(1, int(n ** 0.5) + 1):
            if n % m == 0:
                count += 1
                if n // m != m:
                    count += 1
        return count
    
    answer = 0
    
    for x in [count_gcd(i) for i in range(1, number + 1)]:
        if x > limit:
            answer += power
        else:
            answer += x
    
    return answer