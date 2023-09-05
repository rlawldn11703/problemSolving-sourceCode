from collections import deque
import sys
M,N,H = map(int,sys.stdin.readline().split())
boxes = []
for _ in range(H):
    boxes.append([list(map(int,sys.stdin.readline().split())) for _ in range(N)])
ans = -1
days = [[[0] * M for _ in range(N)] for _ in range(H)]
q = deque([])
for h in range(H):
    for i in range(N):
        for j in range(M):
            days[h][i][j] = boxes[h][i][j] - 1
            if boxes[h][i][j] == 1:
                q.append((i,j,h))
def ck(days):
    global ans
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if days[h][i][j] == -1:
                    return False
                ans = max(ans,days[h][i][j])
    return True

dx,dy,dz = [1,0,-1,0,0,0],[0,1,0,-1,0,0],[0,0,0,0,1,-1]
while q:
    x,y,z = q.popleft()
    for w in range(6):
        nx,ny,nz = x+dx[w],y+dy[w],z+dz[w]
        if nx<0 or nx >= N or ny <0 or ny >= M or nz < 0 or nz >= H:
            continue
        if days[nz][nx][ny] == -1:
            q.append((nx,ny,nz))
            days[nz][nx][ny] = days[z][x][y] + 1
if ck(days):
    print(ans)
else:
    print(-1)
