def check(length, count):
    return length % 2 == 0 and count >= length // 2 \
           or length % 2 == 1 and count >= length // 2 + 1


def convert(s, dic):
    cnt, result, tmp = 0, '', ''

    for i, v in enumerate(s):
        if v.isalpha():
            result += v
        elif v in dic:
            result += dic[v]
            cnt += 1
        elif v not in ('\\', '\''):
            return "I don't understand"
        else:
            tmp += v
            if tmp in dic:
                result += dic[tmp]
                cnt += 1
                tmp = ''

    if check(len(result), cnt):
        return "I don't understand"
    return result


target = {
    '@': 'a', '[': 'c', '!': 'i', ';': 'j', '^': 'n',
    '0': 'o', '7': 't', "\\'": 'v', "\\\\'": 'w'
}

for _ in range(int(input())):
    print(convert(input(), target))
