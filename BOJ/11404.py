import sys
n,m = int(input()),int(input())
dp = [[int(1e9)]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    dp[a][b] = min(dp[a][b],c)
for i in range(1,n+1):
    dp[i][i] = 0
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j])
for i in range(1,n+1):
    for j in range(1,n+1):
        if dp[i][j] >= int(1e9):
            print(0,end=" ")
        else:
            print(dp[i][j],end=" ")
    print()

