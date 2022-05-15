# 실전 문제 2 - 왕실의 나이트(115p)

pos = input()
pos_alpha = int(ord(pos[0])) - int(ord('a')) + 1
pos_num = int(pos[1])

move = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

count = 0
for i in range(len(move)):
    nx = pos_num + move[i][1]
    ny = pos_alpha + move[i][0]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    count += 1

print(count)
