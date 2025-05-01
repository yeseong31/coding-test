import re

from collections import defaultdict
from itertools import product


def solution(user_id, banned_id):
    answer = set()
    bid_dic = defaultdict(set)
    
    for bid in banned_id:
        pid = bid.replace('*', '.')
        pattern = re.compile(pid)
        
        for uid in user_id:
            if pattern.fullmatch(uid):
                bid_dic[bid].add(uid)
        
    uid_list = [bid_dic[bid] for bid in banned_id]
    
    for r in product(*uid_list):
        if len(set(r)) == len(banned_id):
            answer.add(''.join(sorted(set(r))))

    return len(answer)
    