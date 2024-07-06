lst=[]
cnt=[]
for i in range(10):
    lst.append(int(input())%42)
    if cnt.count(lst[i])==0:
        cnt.append(lst[i])
print(len(cnt))