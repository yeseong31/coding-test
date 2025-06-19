def solution(name, yearning, photo):
    dic = dict()
    for n, s in zip(name, yearning):
        dic[n] = s
    
    return [sum(dic[v] for v in p if v in dic) for p in photo]
