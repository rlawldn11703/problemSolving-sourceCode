n,s = map(int,input().split())
arr = list(map(int,input().split()))
arr.append(0)
l,r = 0,1
partial_sum = arr[l]
ans = int(1e9)
while True:
    if partial_sum >= s:
        cnt = r-l
        ans = min(ans,cnt)
        partial_sum -= arr[l]
        l += 1
    else:
        partial_sum += arr[r]
        r += 1
    if r == len(arr):
        break
if ans == int(1e9):
    ans = 0
print(ans)
    
# ans
n, s = map(int, input().split())
a = list(map(int, input().split()))
tot = a[0]
mn = float('inf')

en = 0
for st in range(n):
    while en < n and tot < s:
        en += 1
        if en != n:
            tot += a[en]
    if en == n: # 다 더해도 s가 안되는 경우
        break
    mn = min(mn, en - st + 1)
    tot -= a[st]

if mn == float('inf'):
    mn = 0
print(mn)