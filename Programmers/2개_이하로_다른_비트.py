def solution(numbers):
    answer = []

    for n in numbers:
        bit_n = '0' + bin(n)[2:]
        target_n = list(bit_n)
        i = bit_n.rfind('0')
        target_n[i] = '1'

        if n % 2 == 1:
            target_n[i + 1] = '0'

        answer.append(int(''.join(target_n), 2))

    return answer


numbers = [2, 7]
print(solution(numbers))
