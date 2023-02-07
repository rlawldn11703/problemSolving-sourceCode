import sys
from collections import deque
tc = int(input())
def topology_sort(indegree,n):
    q,ans = deque([]),[]
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        if len(q) >= 2:
            return (0,'?')
        a = q.popleft()
        ans.append(a)
        for b in range(1,n+1):
            if graph[a][b]:
                indegree[b] -= 1
                if indegree[b]==0:
                    q.append(b)
    if len(ans) < n:
        return (0,'IMPOSSIBLE')
    return (1,ans)
for _ in range(tc):
    n = int(input())
    rank = list(map(int,input().split()))
    indegree = [0]*(n+1)
    graph = [[False]*(n+1) for _ in range(n+1)]
    for i in range(n):
        indegree[rank[i]] = i
        for j in range(i+1,n):
            graph[rank[i]][rank[j]] = True
    for _ in range(int(input())):
        a,b = map(int,sys.stdin.readline().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[b] += 1
            indegree[a] -= 1
    result = topology_sort(indegree,n)
    if result[0] == 0:
        print(result[1])
    else:
        [print(i,end=' ') for i in result[1]]
        print()
    
