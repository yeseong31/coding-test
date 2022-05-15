# itertools는 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리이다.

# ---------------------------------------------------------------------------
# permutations(순열)
# 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산한다.
# permutations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.
from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)

# ---------------------------------------------------------------------------
# combinations(조합)
# 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우를 계산한다.
# combinations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.
from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)

# ---------------------------------------------------------------------------
# product(중복을 포함하는 순열)
# permutaitons와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산한다.
# 다만 원소를 중복하여 뽑는다.
# product 객체를 초기화할 때는 뽑고자 하는 데이터의 수를 repeat 속성값으로 넣어준다.
# product는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.
from itertools import product
data = ['A', 'B', 'C']
result = list(product(data, repeat=2))
print(result)

# ---------------------------------------------------------------------------
# combinations_with_replacement(중복을 포함하는 조합)
# combinations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아
# 순서를 고려하지 않고 일렬로 나열하는 모든 경우를 계산한다. 다만 원소를 중복하여 뽑는다.
# combinations_with_replacement는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))
print(result)