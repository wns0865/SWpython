import math
from collections import Counter
arr=[]
total=0
n=int(input())

for i in range(n):
    arr.append(int(input()))
    total+=arr[i]
sarr=sorted(arr)
cnt = Counter(sarr).most_common(2)


print(round(total/n))#평균
print(sarr[(len(arr)//2)])#중앙값
if n>1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else: print(cnt[0][0])#최빈값
else: print(arr[0])
print(max(sarr)-min(sarr))#범위

"""
시간초과 안걸릴려면
import sys

int(sys.stdin.readline())
사용해야됨
"""