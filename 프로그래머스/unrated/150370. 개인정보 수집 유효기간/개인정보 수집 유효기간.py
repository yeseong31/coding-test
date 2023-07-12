def solution(today, terms, privacies):
    answer = []

    expiry_date = dict()
    for term in terms:
        v, k = term.split()
        expiry_date[v] = int(k)

    for i, privacy in enumerate(privacies, 1):
        date, _type = privacy.split()
        y, m, d = map(int, date.split('.'))
        
        # 일수 조정
        d -= 1
        if d == 0:
            d = 28
            m -= 1
            if m == 0:
                m = 12
                y -= 1
        
        # 유효기간 적용
        m += expiry_date[_type]
        if m > 12:
            if m % 12 == 0:
                y += m // 12 - 1
                m = 12
            else:
                y += m // 12
                m %= 12
        # 유효기간 확인
        
        if f'{y}.{str(m).zfill(2)}.{str(d).zfill(2)}' < today:
            answer.append(i)
        
    return sorted(answer)