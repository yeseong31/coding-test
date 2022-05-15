# 순열
# 서로 다른 n개에서 r개를 선택하여 일렬로 나열하는 것

import itertools

data = [1, 2]

for x in itertools.permutations(data, 2):
    print(list(x))
