n, a = map(int, input().split())
arr = []
for i in range(1,n+1):
    arr.append(i)
ans=[]
num=0

for i in range(n):
    num += a - 1
    if num >= len(arr):
        num = num % len(arr)

    ans.append(str(arr.pop(num)))
print("<"+", ".join(ans)+">")