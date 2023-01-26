import sys
def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]
def union(parent,a,b):
    par_a,par_b = find(parent,a),find(parent,b)
    if par_a < par_b:
        parent[par_b] = par_a
    else:
        parent[par_a] = par_b
n,planet = int(input()),[]
parent = [-1]*n
for i in range(n):
    parent[i] = i
for i in range(n):
    x,y,z = map(int,sys.stdin.readline().split())
    planet.append((x,y,z,i))
edges,total = [],0
for i in range(3):
    planet.sort(key=lambda x:x[i])
    for j in range(n-1):
        edges.append((planet[j+1][i]-planet[j][i],planet[j][3],planet[j+1][3]))
edges.sort()
for edge in edges:
    c,a,b = edge
    if find(parent,a) != find(parent,b):
        union(parent,a,b)
        total += c
print(total)
