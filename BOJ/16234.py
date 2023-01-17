from collections import deque
def bfs(s,A,visited):
    global L,R
    dx,dy = [1,0,-1,0],[0,1,0,-1]
    q,n = deque([s]),len(A)
    union,people = [s],A[s[0]][s[1]]
    while q:
        x,y = q.popleft()
        for w in range(4):
            xx,yy = x+dx[w],y+dy[w]
            if xx<0 or xx>=n or yy<0 or yy>=n:
                continue
            if not visited[xx][yy] and L<=abs(A[xx][yy]-A[x][y])<=R:
                union.append((xx,yy))
                q.append((xx,yy))
                visited[xx][yy] = True
                people += A[xx][yy]
    for i,j in union:
        A[i][j] = int(people/len(union))
    return len(union)
n,L,R = map(int,input().split())
A = []
for _ in range(n):
    A.append((list(map(int,input().split()))))
ck,ans = True,-1
while ck:
    visited,ck = [[False]*n for _ in range(n)],False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                if bfs((i,j),A,visited) > 1:
                    ck = True
    ans += 1
print(ans)
