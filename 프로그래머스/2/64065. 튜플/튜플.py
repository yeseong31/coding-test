def solution(s):
    answer = []
    seen = set()

    groups = s[2:-2].split('},{')
    groups.sort(key=lambda g: len(g.split(',')))

    for group in groups:
        for v in group.split(','):
            if v not in seen:
                seen.add(v)
                answer.append(int(v))

    return answer