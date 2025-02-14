import sys
c=int(input())
for i in range(c):
    cnt,avg=0,0
    lst=list(map(int,sys.stdin.readline().split()))
    for j in range(1,len(lst)):
        avg+=lst[j]
    avg=avg/lst[0]
    for k in range(1,len(lst)):
        if lst[k]>avg:
            cnt+=1
    print('{}%'.format(cnt/lst[0]*100))