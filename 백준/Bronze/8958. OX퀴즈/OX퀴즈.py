n=int(input())
for i in range(n):
    res,count=0,0
    lst=list(input())
    for j in range(len(lst)):
        if lst[j]=='O':
            count+=1
            res+=count
        else:
            count=0
    print(res)