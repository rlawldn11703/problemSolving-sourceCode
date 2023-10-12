# 길이 N짜리 수열에서 
# 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이
n,s = map(int,input().split())
arr = list(map(int,input().split()))
l,r = 0,0
partial_sum = arr[l]
ans = int(1e9)

while l<=r:
    if partial_sum >= s:
        cnt = r-l+1
        ans = min(ans,cnt)
        partial_sum -= arr[l]
        l += 1
    else:
        r += 1
        if r == n:
            break
        partial_sum += arr[r]
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