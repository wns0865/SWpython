str="CAMBRIDGE"
a=input()
sa=list(a)
for i in range(len(sa)):
    for j in str:
        if sa[i]==j:
            sa[i]=''
for i in sa:
    print(i,end='')