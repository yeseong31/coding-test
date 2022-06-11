"""
가사 검색(370p)
"""
from bisect import bisect_left, bisect_right


def solution(words, queries):
    # 쿼리와 매칭되는 단어의 수(범위)
    def count(a, left, right):
        return bisect_right(a, right) - bisect_left(a, left)

    # 탐색
    def search():
        result = []
        # 단어를 배열에 저장
        for word in words:
            arr[len(word)].append(word)
            reversed_arr[len(word)].append(word[::-1])  # 문자를 뒤집어서 저장
        # 정렬 (for 이진 탐색)
        for i in range(10001):
            arr[i].sort()
            reversed_arr[i].sort()
        # 정렬된 단어에 대해 쿼리를 하나씩 확인
        for query in queries:
            # 접두사가 '?'인 경우
            if query[0] == '?':
                res = count(reversed_arr[len(query)],
                                        query[::-1].replace('?', 'a'),
                                        query[::-1].replace('?', 'z'))
            # 접미사가 '?'인 경우
            else:
                res = count(arr[len(query)],
                                        query.replace('?', 'a'),
                                        query.replace('?', 'z'))
            # 결과 저장
            result.append(res)
        return result

    arr = [[] for _ in range(10001)]
    reversed_arr = [[] for _ in range(10001)]

    # 탐색 시작
    return search()


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
