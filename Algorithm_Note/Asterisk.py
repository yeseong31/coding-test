# 아스테리스크(*)

# 파이썬에서 *는 언팩으로, 시퀀스 언패킹 연산자로 쓰임
# 즉 시퀀스를 풀어 헤치는 연산자로 쓰이며, 주로 튜플이나 리스트를 언패킹하는 역할로써 쓰임

from collections import Counter

nums = [1, 1, 1, 2, 2, 3]
k = 2

Counter(nums).most_common(k)                # [(1, 3), (2, 2)]
list(zip(*Counter(nums).most_common(k)))    # [(1, 2), (3, 2)]          # 언패킹을 했을 때
list(zip(Counter(nums).most_common(k)))     # [((1, 3), ), ((2, 2), )]  # 언패킹을 하지 않았을 때

# 위의 예제에서처럼 언패킹을 하지 않은 채 zip()으로 묶어 그대로 출력하면 튜플이 풀어지지 않고 그대로 하나의 값처럼 묶여 버리게 됨
# 이 경우 *로 언패킹을 해주어야지만 튜플의 값을 풀어 헤칠 수 있음

# 언패킹한 값만 별도로 출력할 수가 없어 디버깅이 어렵지만,
# 내부적으로는 튜플이 제거되고 [[1, 3], [2, 2]]와 같은 형태로 모두 리스트로 풀어질 것이고,
# 이 값을 zip()으로 묶으면 정상적으로 묶이게 되어 1과 2가 하나의 튜플로 묶이게 되는 것임


# 이해가 되지 않는다면 간단한 예제를 통해 이해해 보자.
fruits = ['lemon', 'pear', 'watermelon', 'tomato']
print(fruits)   # ['lemon', 'pear', 'watermelon', 'tomato']

# fruits 리스트를 출력하면 당연히 리스트의 형태로 출력되는데,
# 이 리스트에서 각 요소의 값만 출력하고 싶다면 다음과 같은 방법을 떠올리게 됨
# (1)
print(fruits[0], fruits[1], fruits[2], fruits[3])
# (2)
for f in fruits:
    print(f)

# 이때 *로 언패킹해주면 다음과 같이 매우 간편하게 출력할 수 있게 됨
print(*fruits)  # lemon pear watermelon tomato


# 이외에도 *는 활용도가 많음
# 언패킹뿐만 아니라 함수의 파라미터가 되었을 때는 반대로 패킹도 가능함
def f(*params):
    print(params)


f('a', 'b', 'c')    # ('a', 'b', 'c')

# 이러한 방식은 Python 3+에서 print() 함수의 기본 동작 원리이기도 함
print('a')              # a
print('a', 'b')         # a b
print('a', 'b', 'c')    # a b c

# 몇 개의 파라미터를 넘기든, 모두 처리가 됨
a, *b = [1, 2, 3, 4]
print(a)    # 1
print(b)    # [2, 3, 4]

*a, b = [1, 2, 3, 4]
print(a)    # [1, 2, 3]
print(b)    # 4

# 변수의 할당 또한 이렇게 *로 묶어서 처리할 수 있음
# 일반적인 변수는 값을 하나만 취하지만 *로 처리하게 되면 나머지 모든 값을 취할 수 있도록 할 수 있음

# *를 하나가 아닌 2개를 쓰는 경우도 있는데, 이는 전혀 다른 동작을 수행함
# 파이썬에서 * 1개는 튜플 또는 리스트 등의 시퀀스 언패킹이고, ** 2개는 다음과 같이 키/값 페어를 언패킹하는 데에 사용됨
date_info = {'year': '2020', 'month': '01', 'day': '7'}
new_info = {**date_info, 'day': '14'}
print(new_info)     # {'year': '2020', 'month': '01', 'day': '14'}
