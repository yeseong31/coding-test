from itertools import product


def solution(users, emoticons):
    answer = []
    emo_len = len(emoticons)

    for perm in list(product([40, 30, 20, 10], repeat=emo_len)):
        prices = [0] * emo_len
        for i in range(emo_len):
            prices[i] = (emoticons[i] * (100 - perm[i])) // 100

        sign_up, sales = 0, 0
        for rate, money in users:
            total = 0
            for i in range(emo_len):
                if rate <= perm[i]:
                    total += prices[i]
            if money <= total:
                sign_up += 1
            else:
                sales += total
            answer.append((sign_up, sales))

    answer.sort(key=lambda x: (-x[0], -x[1]))
    return answer[0]