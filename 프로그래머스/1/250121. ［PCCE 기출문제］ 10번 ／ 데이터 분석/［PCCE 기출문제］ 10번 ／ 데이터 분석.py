def solution(data, ext, val_ext, sort_by):
    names = {
        'code': 0,
        'date': 1,
        'maximum': 2,
        'remain': 3,
    }
    
    answer = [d for d in data if d[names[ext]] < val_ext]
    return sorted(answer, key=lambda x: x[names[sort_by]])
