# 로그 파일 재정렬(148p)


# 로그의 가장 앞은 '식별자'
# 문자 로그가 숫자 로그보다 앞
# 문자가 동일할 경우에 식별자 순으로
# 숫자 로그는 입력 순으로
def reorderLogFiles(logs: list[str]) -> list[str]:
    alpha, num = [], []
    for log in logs:
        if log.split()[1].isdigit():
            num.append(log)
        else:
            alpha.append(log)
    alpha.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return alpha + num


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(reorderLogFiles(logs))
# ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
