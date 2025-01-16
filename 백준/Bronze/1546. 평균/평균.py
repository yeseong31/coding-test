import sys
n=int(input())
lst=list(map(int,sys.stdin.readline().split()))
sum=0
mx=max(lst)
for i in range(n):
    lst[i]=lst[i]/mx*100
    sum+=lst[i]
print(sum/n)