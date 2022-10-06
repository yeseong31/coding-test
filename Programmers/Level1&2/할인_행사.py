import copy


def solution(want, number, discount):
    answer = 0
    check = copy.deepcopy(number)
    left = 0
    total = 10

    idx = dict()
    for i, (w, n) in enumerate(zip(want, number)):
        idx[w] = i

    for right, v in enumerate(discount):
        if v not in want:
            continue
        if number[idx[v]] > 0:
            number[idx[v]] -= 1
            total -= 1
        check[idx[v]] -= 1
        if total != 0:
            continue
        while left < right:
            if discount[left] not in want:
                left += 1
                continue
            if right - left <= 9:
                number[idx[discount[left]]] += 1
                total += 1
            if check[idx[discount[left]]] == 0:
                if right - left == 9:
                    answer += 1
                break
            check[idx[discount[left]]] += 1
            left += 1
    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "dd", "banana"]))
print(solution(["banana"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))
