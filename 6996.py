"""
n=int(input())
i=0
cnt=0
result=0
while i<n :
    a,b=list(input().split())
    ar = set(a)
    for j in ar :
                 cnt=b.count(j)
                 result+=cnt
    if result==len(a) and len(a)==len(b) :
        print (a+" & "+b+" are anagrams.")
    else :
        print(a + " & " + b + " are NOT anagrams.")
    result=0
    i+=1

"""
n=int(input())
i=0
while i<n :
    a,b=input().split()
    ar = sorted(list(a))
    br = sorted(list(b))

    if ar == br:
        print(a + " & " + b + " are anagrams.")
    else:
        print(a + " & " + b + " are NOT anagrams.")
    i+=1