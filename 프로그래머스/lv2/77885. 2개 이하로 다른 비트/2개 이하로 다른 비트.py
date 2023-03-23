def solution(numbers):
    answer = []
    for n in numbers:
        if n % 2 == 0:
            answer.append(n + 1)
            continue
        target = f'{0}{bin(n)[2:]}'
        r = target.rindex('0')
        answer.append(int(f'{target[:r]}{10}{target[r + 2:]}', 2))
    return answer
