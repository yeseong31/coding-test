def solution(lottos, win_nums):
    correct = 0
    cnt_0 = lottos.count(0)

    # 맞힌 숫자에 따라 순위 결정
    rank = [6, 6, 5, 4, 3, 2, 1]

    for lotto_num in lottos:
        # 맞힌 숫자 카운트
        if lotto_num in win_nums:
            correct += 1

    return rank[correct + cnt_0], rank[correct]