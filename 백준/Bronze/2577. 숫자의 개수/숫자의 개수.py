a=int(input())
b=int(input())
c=int(input())
res=a*b*c
lst=[0,0,0,0,0,0,0,0,0,0]
while True:
    lst[res%10] += 1
    res=res//10
    if res == 0:
        break
for i in range(10):
    print(lst[i])