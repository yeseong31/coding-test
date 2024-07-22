import collections
import sys

input = sys.stdin.readline
n = int(input())
dic = collections.defaultdict(int)

for _ in range(n):
    dic[int(input())] += 1

sorted_dic = sorted(dic.items())

for i in range(len(sorted_dic)):
    for j in range(sorted_dic[i][1]):
        print(sorted_dic[i][0])