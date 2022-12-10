import re


target = input().strip()
pattern = re.sub('~', '+', '(100~1~|01)~')
match = re.compile(pattern)
print('SUBMARINE' if re.fullmatch(match, target) else 'NOISE')