from collections import deque


def solution(begin, target, words):
    def bfs(word):
        q = deque([(word, 0)])
        check = set(word, )
        while q:
            v, c = q.popleft()
            if v == target:
                return c
            for w in words:
                count = 0
                for a, b in zip(v, w):
                    if a == b:
                        count += 1
                if count == len(v) - 1 and w not in check:
                    check.add(w)
                    q.append((w, c + 1))

    if target not in words:
        return 0
    return bfs(begin)


begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))
