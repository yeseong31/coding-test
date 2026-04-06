def solution(message, spoiler_ranges):
    spoiler_words = set()
    normal_words = set()

    is_spoiler = [False] * len(message)
    for start, end in spoiler_ranges:
        for i in range(start, end + 1):
            is_spoiler[i] = True

    sb = []
    flag = False

    for i, c in enumerate(message):
        if c == ' ':
            if sb:
                word = ''.join(sb)
                if flag and word not in normal_words:
                    spoiler_words.add(word)
                else:
                    normal_words.add(word)
                sb = []
                flag = False
        else:
            sb.append(c)
            if is_spoiler[i]:
                flag = True

    if sb:
        word = ''.join(sb)
        if flag and word not in normal_words:
            spoiler_words.add(word)
        else:
            normal_words.add(word)

    answer = 0
    for word in spoiler_words:
        if word not in normal_words:
            answer += 1

    return answer