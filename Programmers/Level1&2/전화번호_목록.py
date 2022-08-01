def solution(phone_book):
    dic = {}
    for book in phone_book:
        dic[book] = 1
    for book in phone_book:
        tmp = ''
        for b in book[:-1]:
            tmp += b
            if tmp in dic and tmp != book:
                return False
    return True