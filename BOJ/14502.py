from itertools import combinations
from collections import deque
from copy import deepcopy
def bfs(B,virus,n,m):
    dx,dy = [1,0,-1,0],[0,1,0,-1]
    visited = [[False]*m for _ in range(n)]
    Board,q,cnt = deepcopy(B),deque([]),0
    for i,j in virus:
        q.append((i,j))
        visited[i][j] = True
        while q:
            x,y = q.popleft()
            for w in range(4):
                xx,yy = x+dx[w],y+dy[w]
                if xx<0 or xx>=n or yy<0 or yy>=m:
                    continue
                if not visited[xx][yy] and Board[xx][yy]=='0':
                    Board[xx][yy] = '2'
                    visited[xx][yy] = True
                    q.append((xx,yy))
    for i in range(n):
        for j in range(m):
            if Board[i][j]=='0':
                cnt += 1
    return cnt
n,m = map(int,input().split())
Board,empty,virus = [],[],[]
for i in range(n):
    Board.append(input().split())
    for j in range(m):
        if Board[i][j]=='0':
            empty.append((i,j))
        if Board[i][j]=='2':
            virus.append((i,j))
ans = -1
for loc in combinations(empty,3):
    for x,y in loc:
        Board[x][y] = '1'
    ans = max(ans,bfs(Board,virus,n,m))
    for x,y in loc:
        Board[x][y] = '0'
print(ans)
