def solution(n, words):
    used = set()
    used.add(words[0])
    prev = words[0][-1]
    cnt = 1

    for word in words[1:]:
        if word in used or prev != word[0]:
            return cnt % n + 1, cnt // n + 1

        used.add(word)
        cnt += 1
        prev = word[-1]

    return 0, 0