import copy

INF = int(1e6)


def flip_switch(arr, a, b, c=None):
    arr[a] = 1 - arr[a]
    arr[b] = 1 - arr[b]
    if c is None:
        return
    arr[c] = 1 - arr[c]


def solution():
    n = int(input())
    lst1 = list(map(int, input()))
    target = list(map(int, input()))

    if lst1 == target:
        return 0
    lst2 = copy.deepcopy(lst1)

    answer = INF
    for i in range(2):
        current = lst1 if i == 0 else lst2
        cnt = 0
        if i == 0:
            flip_switch(current, 0, 1)
            cnt += 1
        for j in range(1, n - 1):
            if current[j - 1] != target[j - 1]:
                flip_switch(current, j - 1, j, j + 1)
                cnt += 1
        if current[n - 2] != target[n - 2]:
            flip_switch(current, n - 2, n - 1)
            cnt += 1
        if current == target:
            answer = min(answer, cnt)

    if answer == INF:    
        return -1
    return answer


print(solution())