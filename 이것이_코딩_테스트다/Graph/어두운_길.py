import sys
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
n,m = map(int,input().split())
parent = [0]*n
for i in range(n):
    parent[i] = i
org,edges = 0,[]
for _ in range(m):
    x,y,z = map(int,sys.stdin.readline().split())
    org += z
    edges.append((z,x,y))
edges.sort()
cost = 0
for edge in edges:
    z,x,y = edge
    if find(parent,x) != find(parent,y):
        union(parent,x,y)
        cost += z
print(org-cost)
