def use_fork(storage, box):
    dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
    index = []
    
    for x in range(1, len(storage) - 1):
        for y in range(1, len(storage[0]) - 1):
            if storage[x][y] != box:
                continue
                
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if storage[nx][ny] == '0':
                    index.append((x, y)) 
                    break
    
    for x, y in index:
        storage[x][y] = '0'
        is_outside(storage, x, y)

        
def use_crane(storage, box):
    for x in range(1, len(storage) - 1):
        for y in range(1, len(storage[0]) - 1):
            if storage[x][y] == box:
                storage[x][y] = '#'
                is_outside(storage, x, y)

                
def is_outside(storage, x, y):
    dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
    outside = False

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if storage[nx][ny] == '0':
            storage[x][y] = '0'
            outside = True         
            break
    
    if outside:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if storage[nx][ny] == '#':
                storage[nx][ny] = '0'
                is_outside(storage, nx, ny)

                
def solution(storage, requests):
    answer = 0
    
    exp_storage = [['0' for _ in range(len(storage[0]) + 2)] for _ in range(len(storage) + 2)]
    for x in range(len(storage)):
        for y in range(len(storage[0])):
            exp_storage[x + 1][y + 1] = storage[x][y]

    for q in requests:
        if len(q) == 1:
            use_fork(exp_storage, q)
        else:
            use_crane(exp_storage, q[0])
    
    for x in range(len(storage)):
        for y in range(len(storage[0])):
            if exp_storage[x + 1][y + 1] not in ['0', '#']:
                answer += 1
    
    return answer