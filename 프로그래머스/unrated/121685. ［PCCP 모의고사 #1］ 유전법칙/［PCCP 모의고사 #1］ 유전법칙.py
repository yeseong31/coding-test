def solution(queries):
    answer = []
    gene = {'00': 'RR', '01': 'Rr', '10': 'Rr', '11': 'rr'}

    for n, p in queries:
        n = (n - 1) * 2
        p -= 1
        target = f'{bin(p)[2:].zfill(n)}'

        check = False
        for t in [target[i:i + 2] for i in range(0, len(target), 2)]:
            if t in ('00', '11'):
                check = True
                answer.append(gene[t])
                break
        if not check:
            answer.append('Rr')

    return answer
