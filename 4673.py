n = set(range(1, 10000))
arr= set()
for i in n:
    for j in str(i):
            i += int(j)
    arr.add(i)
ans = n - arr
sans=sorted(ans)
for ans in sans:
    print(ans)