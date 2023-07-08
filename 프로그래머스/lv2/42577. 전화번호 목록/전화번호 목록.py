def solution(phone_book):
    phone_book.sort()
    for i in range(1, len(phone_book)):
        p1, p2 = phone_book[i - 1], phone_book[i]
        if p2[:len(p1)] == p1:
            return False
    return True