from collections import defaultdict


def solution(record):
    users = defaultdict(str)
    events = []
    txt = ('님이 들어왔습니다.', '님이 나갔습니다.')
    
    for r in record:
        event, *userinfo = r.split()
        if event == 'Enter':
            events.append((userinfo[0], 0))
            users[userinfo[0]] = userinfo[1]
        elif event == 'Leave':
            events.append((userinfo[0], 1))
        else:
            users[userinfo[0]] = userinfo[1]
    
    return [f'{users[uid]}{txt[i]}' for uid, i in events]