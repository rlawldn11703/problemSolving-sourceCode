n,m,k = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort(reverse=True)
total,ans = 0,0
while total < m:
    ans += (arr[0]*(m -total if k > m-total else k))
    total += m -total if k > m-total else k
    if total < m:
        ans += arr[1]
        total += 1
print(ans)
# Revised
n,m,k = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort(reverse=True)
ans,cnt = 0, int(m/(k+1))*k + m%(k+1)
ans += arr[0]*cnt
ans += arr[1]*(m-cnt)
print(ans)
