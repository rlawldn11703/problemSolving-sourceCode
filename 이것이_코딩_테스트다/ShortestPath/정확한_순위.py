n,m = map(int,input().split())
graph = [[int(1e6)]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i] = 0
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
ans = 0
for i in range(1,n+1):
    cnt = 0
    for j in range(1,n+1):
        if graph[i][j] != int(1e6) or graph[j][i] != int(1e6):
            cnt += 1
    if cnt == n:
        ans += 1
print(ans)
