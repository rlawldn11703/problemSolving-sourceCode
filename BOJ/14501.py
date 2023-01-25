n = int(input())
info = []
dp = [0]*(n+1)
for _ in range(n):
    info.append(list(map(int,input().split())))
for i in range(n+1):
    dp[i] = dp[i-1]
    for j in range(i):
        t,p = info[j][0],info[j][1]
        if j+t==i:
            dp[i] = max(dp[i],dp[j]+p)
print(dp[-1])
