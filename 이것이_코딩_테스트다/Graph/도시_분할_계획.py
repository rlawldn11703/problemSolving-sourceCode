def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]
def union(parent,a,b):
    a,b = find(parent,a),find(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
N,M = map(int,input().split())
parent = [i for i in range(N+1)]
edges,result,max_cost = [],0,0
for _ in range(M):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))
edges.sort()
print(edges)
for edge in edges:
    cost,a,b = edge
    if find(parent,a) != find(parent,b):
        union(parent,a,b)
        result += cost
        max_cost = cost
print(result-max_cost)
