import collections


def solution(begin, target, words):
    def bfs(start):
        q = collections.deque()
        q.append((start, 0))

        checked = set()
        checked.add(start)

        while q:
            v, c = q.popleft()
            if v == target:
                return c
            for i, w in enumerate(words):
                count = 0
                for a, b in zip(v, w):
                    if a == b:
                        count += 1
                if count == len(v) - 1 and w not in checked:
                    checked.add(w)
                    q.append((w, c + 1))

    if target not in words:
        return 0
    return bfs(begin)


begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))
