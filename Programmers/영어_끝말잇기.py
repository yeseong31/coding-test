def solution(n, words):
    # 이전에 등장했던 단어는 사용할 수 없음
    used = set()
    used.add(words[0])
    prev = words[0][-1]
    cnt = 1

    for word in words[1:]:
        # 이전에 등장했거나 끝말잇기가 아닌 단어라면
        if word in used or prev != word[0]:
            return [cnt % n + 1, cnt // n + 1]

        used.add(word)
        cnt += 1
        prev = word[-1]

    return [0, 0]


n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, words))