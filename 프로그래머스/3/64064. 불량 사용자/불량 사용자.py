from re import fullmatch


def dfs(index, banned, banned_dict, result):
    if index == len(banned_dict):
        result.add(tuple(sorted(banned)))
        return
    
    for bid in banned_dict[index]:
        if bid in banned:
            continue
        
        banned.add(bid)
        dfs(index + 1, banned, banned_dict, result)
        banned.remove(bid)


def solution(user_id, banned_id):
    banned_id = [bid.replace('*', '.') for bid in banned_id]
    banned_dict = [list(uid for uid in user_id if fullmatch(bid, uid)) for bid in banned_id]
    
    result = set()
    dfs(0, set(), banned_dict, result)
    return len(result)
    