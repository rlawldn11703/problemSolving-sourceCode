import heapq
n,m,c = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y,t = map(int,input().split())
    graph[x].append((y,t))
INF = int(1e9)
distance = [INF]*(n+1)
def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist,node = heapq.heappop(q)
        if distance[node]<dist:
            continue
        for i in graph[node]:
            cost = dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(c)
cnt,time = 0,0
for i in range(1,n+1):
    if distance[i]==INF or i==c:
        continue
    cnt += 1
    time = max(time,distance[i])
print(cnt,time)
