# 플로이드워셜을 돌리고 노드별로 수색범위보다 작거나 같은 거리에 있는 점들의 아이템 수 합을 구해 최대값을 출력하는 코드
n,m,r = map(int,input().split())
num_item = list(map(int,input().split()))
dist = [[int(1e9)]*(n+1) for _ in range(n+1)]
for _ in range(r):
    a,b,l = map(int,input().split())
    dist[a][b] = dist[b][a]  = l
for i in range(1,n+1):
    dist[i][i] = 0
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            tmp = dist[i][k] + dist[k][j]
            if tmp < dist[i][j]:
                dist[i][j] = tmp
ans = 0
for i in range(1,n+1): # 낙하할 지점
    item = 0
    for j in range(1,n+1): # 도달 가능한 지점
        if dist[i][j] <= m:
            item += num_item[j-1]
    ans = max(ans,item)
print(ans)

# answer
n,m,r = map(int,input().split())
item = [0] + list(map(int, input().split()))

d = [[float('inf')]*(n+1) for _ in range(n+1)]
nxt = [[0]*(n+1) for _ in range(n+1)]
# to keep track of the next node in the shortest path between any two nodes in the graph.

for i in range(1, n+1):
    d[i][i] = 0

for _ in range(r):
    x, y, dist = map(int, input().split())
    d[x][y] = dist
    d[y][x] = dist
    nxt[x][y] = y # x에서 y로 가는 최단거리동안 방문할 다음 노드
    nxt[y][x] = x # y에서 x로 가는 최단거리동안 방문할 다음 노드

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            tmp = d[i][k] + d[k][j]
            if tmp < d[i][j]: # 더 적은 비용으로 움직일 수 있다면 -> 최단 거리 갱신
                d[i][j] = tmp
                nxt[i][j] = nxt[i][k] 

ans = 0
for i in range(1, n+1): # 낙하할 지점
    vis = [False]*(n+1) 
    for j in range(1, n+1): # 방문할 지점
        if d[i][j] > m:
            continue
        # 방문 가능한 지 확인하기
        cur = i
        while cur != j:
            vis[cur] = True
            cur = nxt[cur][j]
        vis[j] = True
    tmp = sum(item[j] for j in range(1, n+1) if vis[j]) # 얻을 수 있는 아이템 개수 더하기
    ans = max(ans, tmp)

print(ans)
