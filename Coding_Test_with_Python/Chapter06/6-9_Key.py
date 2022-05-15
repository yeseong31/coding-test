# sorted()나 sort()를 이용할 때에는 key 매개변수를 입력으로 받을 수 있다.


array = [('바나나', 2), ('사과', 5), ('당근', 3)]


def setting(data):
    return data[1]


result = sorted(array, key=setting)
print(result)

# 정렬 라이브러리는 항상 최악의 경우에도 시간 복잡도 O(NlogN)을 보장한다.
# 파이썬은 정확히는 '병합 정렬'과 '삽입 정렬'의 아이디어를 더한 하이브리드 방식의 정렬 알고리즘을 사용한다.
