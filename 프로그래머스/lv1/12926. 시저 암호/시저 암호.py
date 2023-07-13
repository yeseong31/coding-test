def solution(s, n):
    answer = []
    for c in s:
        if c == ' ':
            answer.append(' ')
            continue
        v = ord('a') if c.islower() else ord('A')
        answer.append(chr((ord(c) - v + n) % 26 + v))
                
    return ''.join(answer)