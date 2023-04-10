from collections import deque


n, k = map(int, input().split())
s = ''.join(list(map(str, input().split())))

target = ''.join(str(x) for x in range(1, n + 1))
checked = {s, }
q = deque([(s, 0)])

answer = -1
while q:
    case, cnt = q.popleft()
    if case == target:
        answer = cnt
        break
    for i in range(n - k + 1):
        tmp = f'{case[:i]}{case[i:i+k][::-1]}{case[i+k:]}'
        if tmp in checked:
            continue
        checked.add(tmp)
        q.append((tmp, cnt + 1))

print(answer)
