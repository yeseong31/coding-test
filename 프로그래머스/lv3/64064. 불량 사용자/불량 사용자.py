from re import fullmatch
from itertools import permutations


def solution(user_id, banned_id):
    answer = set()
    bids = ' '.join(banned_id).replace('*', '.')
    
    # 응모자 순열
    for uids in permutations(user_id, len(banned_id)):
        # 응모자와 불량 사용자 매칭
        if fullmatch(bids, ' '.join(uids)):
            # 제재 아이디 목록 내용이 동일하면 같음 -> 정렬 사용
            answer.add(' '.join(sorted(uids)))
        
    return len(answer)
