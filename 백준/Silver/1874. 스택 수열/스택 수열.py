stack = []
result = []
cur = 0
check = True

n = int(input())
for _ in range(n):
    target = int(input())
    
    # cur보다 target이 크면 그만큼 stack에 숫자를 추가해야 함
    while cur < target:
        cur += 1
        stack.append(cur)
        result.append('+')
    # 스택 최상단 숫자와 target이 같다면 pop() 수행
    if stack[-1] == target:
        stack.pop()
        result.append('-')
    else:
        check = False
        break

if not check:
    print('NO')
else:
    print('\n'.join(result))
     
# 8 / 4 3 6 8 7 5 2 1
# 1                +    
# 1 2              +    
# 1 2 3            +    
# 1 2 3 4          +    
# 1 2 3            -    4
# 1 2              -    3
# 1 2 5            +    
# 1 2 5 6          +    
# 1 2 5            -    6
# 1 2 5 7          +    
# 1 2 5 7 8        +        
# 1 2 5 7          -    8
# 1 2 5            -    7
# 1 2              -    5
# 1                -    2    
#                  -    1