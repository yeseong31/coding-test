# 조합
# 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것

import itertools

data = [1, 2, 3]

for x in itertools.combinations(data, 2):
    print(list(x), end=' ')
