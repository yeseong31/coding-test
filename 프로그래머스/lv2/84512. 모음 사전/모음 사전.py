def solution(word):
    def make_dic(p, depth):
        if depth > 5:
            return
        if p != '':
            data.append(p)
        for x in 'AEIOU':
            make_dic(f'{p}{x}', depth + 1)
    
    answer = 0
    data = []
    make_dic('', 0)
    
    for i in range(len(data)):
        if data[i] == word:
            return i + 1
    
    return answer