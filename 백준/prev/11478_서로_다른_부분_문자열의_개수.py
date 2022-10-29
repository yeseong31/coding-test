import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)

check_set = set()

for i in range(n):
    for j in range(i, n + 1):
        target_str = s[i:j]
        if target_str not in check_set:
            check_set.add(target_str)

print(len(check_set) - 1)

# 메모리를 많이 잡아 먹는 코드라 수정 필요 (240168 KB)
