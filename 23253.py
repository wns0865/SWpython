import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[]
er=0
for _ in range(m):
    x=int( input())
    a= list(map(int, input().split()))
    for i in range(x-1):
        if a[i]<a[i+1]:
            er+=1
            break
if er>0:
    print("No")
else:print("Yes")