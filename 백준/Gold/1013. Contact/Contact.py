import re


pattern = '(100+1+|01)+'
for _ in range(int(input())):
    print('YES' if re.fullmatch(re.compile(pattern), input().strip()) else 'NO')
