def solution(today, terms, privacies):
    def calcul_date(y, m, d, p) -> str:
        d -= 1
        if d == 0:
            d = 28
            m -= 1
            if m == 0:
                m = 12
                y -= 1
        m += p
        if m > 12:
            if m % 12 == 0:
                y += m // 12 - 1
                m = 12
            else:
                y += m // 12
                m %= 12
        return f'{y}.{str(m).zfill(2)}.{str(d).zfill(2)}'
    
    answer = []
    periods = {t[0]: int(t[2:]) for t in terms}

    for i, privacy in enumerate(privacies, 1):
        target = privacy.split()
        year, month, day = map(int, target[0].split('.'))
        
        date = calcul_date(year, month, day, periods[target[-1]])
        if date < today:
            answer.append(i)
        
    return sorted(answer)
