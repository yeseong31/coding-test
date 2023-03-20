from collections import defaultdict


def solution(record):
    result = []
    users = defaultdict(str)
    
    for r in record:
        _type, *info = r.split()
        if _type == 'Leave':
            result.append((info[0], '님이 나갔습니다.'))
            continue
        users[info[0]] = info[1]
        if _type == 'Enter':
            result.append((info[0], '님이 들어왔습니다.'))
            
    return [f'{users[uid]}{txt}' for uid, txt in result]