def solution(queries):
    answer = []
    gene = {'00': 'RR', '11': 'rr'}  # 비트 연산 이용

    for n, p in queries:
        n, p = (n - 1) * 2, p - 1
        target = bin(p)[2:].zfill(n)
        check = False

        for t in [target[i:i + 2] for i in range(0, len(target), 2)]:
            if t in gene:
                check = True
                answer.append(gene[t])
                break
        if not check:
            answer.append('Rr')

    return answer


print(solution([[3, 1], [2, 3], [3, 9]]))
