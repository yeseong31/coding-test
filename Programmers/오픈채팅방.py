def solution(record):
    uid = {}
    result = []

    for rec in record:
        r = rec.split()
        if r[0] == 'Enter':
            uid[r[1]] = r[2]
            result.append((r[1], '님이 들어왔습니다.'))
        elif r[0] == 'Leave':
            result.append((r[1], '님이 나갔습니다.'))
        else:
            uid[r[1]] = r[2]

    return [f'{uid[result[i][0]] + result[i][1]}' for i in range(len(result))]