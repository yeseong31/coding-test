from bisect import bisect_left, bisect_right


def solution(words, queries):
    answer = []
    arr = [[] for _ in range(10001)]
    reverse_arr = [[] for _ in range(10001)]

    for word in words:
        length = len(word)
        arr[length].append(word)
        reverse_arr[length].append(word[::-1])

    for i in range(10001):
        arr[i].sort()
        reverse_arr[i].sort()

    for query in queries:
        res, length = 0, len(query)
        if arr[length] != 0:
            if query[0] != '?':
                res = bisect_right(arr[length],
                                   query.replace('?', 'z')) - bisect_left(arr[length], query.replace('?', 'a'))
            else:
                res = bisect_right(reverse_arr[length],
                                   query[::-1].replace('?', 'z')) - bisect_left(reverse_arr[length],
                                                                                query[::-1].replace('?', 'a'))
        answer.append(res)

    return answer
