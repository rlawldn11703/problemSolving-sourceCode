import heapq,collections
N,M,X = map(int,input().split())
graph = collections.defaultdict(list)
for _ in range(M):
    start,end,time = map(int,input().split())
    graph[start].append((end,time))
def dijkstra(graph,s,e):
    dist = [int(1e9)]*(N+1)
    dist[s] = 0
    heap = []
    heapq.heappush(heap,(0,s))
    while heap:
        cost,node = heapq.heappop(heap)
        if dist[node] < cost: # 이미 더 최소 비용으로 그곳에 도달할 수 있으면 갱신 X
            continue
        for adj, c in graph[node]:
            if cost+c < dist[adj]:
                dist[adj] = cost+c
                heapq.heappush(heap,(cost+c,adj))
    return dist[e]

ans = 0
for i in range(1,N+1):
    one_way = dijkstra(graph,i,X)
    round = dijkstra(graph,X,i)
    distance = one_way + round
    ans = max(ans,distance)
print(ans)
        
