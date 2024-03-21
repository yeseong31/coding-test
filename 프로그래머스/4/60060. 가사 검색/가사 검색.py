from bisect import bisect_left, bisect_right


def solution(words, queries):
    answer = []
    tries = [[] for _ in range(10001)]
    reverse_tries = [[] for _ in range(10001)]
    check_length = set()
    
    for word in words:
        length = len(word)
        tries[length].append(word)
        reverse_tries[length].append(word[::-1])
        check_length.add(length)
        
    for key in check_length:
        tries[key].sort()
        reverse_tries[key].sort()
        
    for query in queries:
        length = len(query)
        
        if not tries[length]:
            answer.append(0)
            continue
        
        if query[0] != '?':
            left = bisect_left(tries[length], query.replace('?', 'a'))
            right = bisect_right(tries[length], query.replace('?', 'z'))
        else:
            left = bisect_left(reverse_tries[length], query[::-1].replace('?', 'a'))
            right = bisect_right(reverse_tries[length], query[::-1].replace('?', 'z'))
            
        answer.append(right - left)
            
    return answer
