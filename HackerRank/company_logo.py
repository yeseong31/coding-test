from collections import Counter

if __name__ == '__main__':
    s = input()
    target = Counter(s)
    for c in sorted(Counter(s), key=lambda x: (-target[x], x))[:3]:
        print(c, target[c])
