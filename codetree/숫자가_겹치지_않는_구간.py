n = int(input())
arr = list(map(int,input().split()))
num_set = set()
s,e = 0,0
ans = 0
while s <= e:
    if arr[e] in num_set:
        ans = max(ans,e-s)
        num_set.remove(arr[s])
        s += 1
    else:
        num_set.add(arr[e])
        e += 1
    if e == n :
        ans = max(ans,e-s)
        break
print(ans)
        