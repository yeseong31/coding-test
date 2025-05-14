INF = int(1e9)


def solution(arr):
    max_dp = [[-INF] * 202 for _ in range(202)]
    min_dp = [[INF] * 202 for _ in range(202)]
    return get_max(0, len(arr), arr, max_dp, min_dp)


def get_max(start, end, arr, max_dp, min_dp):
    if max_dp[start][end] != -INF:
        return max_dp[start][end]
    if end - start == 1:
        return int(arr[start])
    
    result = -INF
    
    for i in range(start + 1, end, 2):
        if arr[i] == '+':
            v1 = get_max(start, i, arr, max_dp, min_dp)
            v2 = get_max(i + 1, end, arr, max_dp, min_dp)
            v = v1 + v2
        else:
            v1 = get_max(start, i, arr, max_dp, min_dp)
            v2 = get_min(i + 1, end, arr, max_dp, min_dp)
            v = v1 - v2
        
        result = max(result, v)
    
    max_dp[start][end] = result
    return result


def get_min(start, end, arr, max_dp, min_dp):
    if min_dp[start][end] != INF:
        return min_dp[start][end]
    if end - start == 1:
        return int(arr[start])
    
    result = INF
    
    for i in range(start + 1, end, 2):
        if arr[i] == '+':
            v1 = get_min(start, i, arr, max_dp, min_dp)
            v2 = get_min(i + 1, end, arr, max_dp, min_dp)
            v = v1 + v2
        else:
            v1 = get_min(start, i, arr, max_dp, min_dp)
            v2 = get_max(i + 1, end, arr, max_dp, min_dp)
            v = v1 - v2
    
        result = min(result, v)
    
    min_dp[start][end] = result
    return result
