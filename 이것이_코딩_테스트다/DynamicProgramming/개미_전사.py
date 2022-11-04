n = int(input())
arr = list(map(int,input().split()))
dp = [0] * n
dp[0],dp[1] = arr[0],max(arr[0],arr[1])
for i in range(2,n):
    dp[i] = max(dp[i-1],dp[i-2]+arr[i])
print(dp[-1])
