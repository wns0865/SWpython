a=input().upper() #aaabbbccc
b=list(set(a))    #abc
cntlist=[]
for i in b:       # a ~c
    cnt=a.count(i) # cnt=a의 i개수 
    cntlist.append(cnt)#  cntlist에 cnt값 

if cntlist.count(max(cntlist))>1: #cntlist의 최대값의 개수가 2개 이상이면 ? 출력
    print('?')
else:
    ans=cntlist.index(max(cntlist))
    print(b[ans])