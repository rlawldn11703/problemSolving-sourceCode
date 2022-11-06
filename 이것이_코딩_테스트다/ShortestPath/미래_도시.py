# 다익스트라 
import heapq
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
x, k =map(int,input().split())
INF = int(1e9)
def dijkstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist,node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for i in graph[node]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q,(cost,i))
    return distance
num1,num2 = dijkstra(1)[k],dijkstra(k)[x]
if num1 == INF or num2==INF:
    print(-1)
else:
    print(num1+num2)

# 플로이드 워셜
n,m = map(int,input().split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j] = 0
for _ in range(m):
    a,b= map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
x, k =map(int,input().split())
distance = graph[1][k]+graph[k][x]
if distance >= INF:
    print(-1)
else:
    print(distance)
