# Mine
import sys
n,m = map(int,input().split())
dp = [10001] *(m+1)
dp[0] = 0
arr = []
for _ in range(n):
    money = int(sys.stdin.readline().rstrip())
    if money > m:
        continue
    dp[money] = 1
    arr.append(money)
for i in range(1,m+1):
    for j in arr:
        if i+j <= m:
            dp[i+j] = min(dp[i+j],dp[i]+1)
if dp[m]>10000:
    print(-1)
else:
    print(dp[m])
  
# Revised
n,m = map(int,input().split())
dp = [10001] *(m+1)
dp[0] = 0
arr = []
for _ in range(n):
    money = int(sys.stdin.readline().rstrip())
    arr.append(money)
for i in range(n):
    for j in range(arr[i],m+1):
        if dp[j-arr[i]] != 10001:
            dp[j] = min(dp[j],dp[j-arr[i]]+1)
if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
    
