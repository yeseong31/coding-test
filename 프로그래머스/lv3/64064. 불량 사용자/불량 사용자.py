import re


def solution(user_id, banned_id):
    def search(index: int, visited: int, answer: set, patterns: list) -> None:
        if index == len(patterns):
            answer.add(visited)
            return
        for i in range(len(user_id)):
            if visited & (1 << i) > 0 or not re.fullmatch(patterns[index], user_id[i]):
                continue
            search(index + 1, visited | (1 << i), answer, patterns)

    answer = set()
    patterns = [x.replace('*', '.') for x in banned_id]
    search(0, 0, answer, patterns)
    return len(answer)