from collections import defaultdict, deque


def build_keys(condition):
    result = []
    q = deque([(0, [])])
    
    while q:
        index, current_keys = q.popleft()
        
        if index == len(condition):
            result.append(''.join(current_keys))
            continue
        
        q.append((index + 1, current_keys + [condition[index]]))
        q.append((index + 1, current_keys + ['-']))
    
    return result


def binary_search(key, score, scores):
    if not scores:
        return 0
    
    start, end = 0, len(scores) - 1
    
    while start < end:
        mid = (start + end) // 2
        if scores[mid] >= score:
            end = mid
        else:
            start = mid + 1
    
    if scores[start] < score:
        return len(scores)
    return start


def solution(info, query):
    answer = []
    dic = defaultdict(list)
    
    for condition in [x.split(' ') for x in info]:
        score = int(condition.pop())
        for key in build_keys(condition):
            dic[key].append(score)
        
    for key in dic:
        dic[key].sort()

    for q in query:
        target = q.replace('and', '').split(' ')
        
        score = int(target.pop())
        key = ''.join(target)
        
        answer.append(len(dic[key]) - binary_search(key, score, dic[key]))
    
    return answer
