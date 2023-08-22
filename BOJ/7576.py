from collections import deque
M,N = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
dist = [[0]*M for _ in range(N)]
q = deque([])
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            q.append((i,j))
dx,dy = [1,0,-1,0],[0,1,0,-1]
max_cnt = 0
while q:
    x,y = q.popleft()
    for dir in range(4):
        nx,ny = x+dx[dir],y+dy[dir]
        if nx < 0 or nx >= N or ny <0 or ny >= M:
            continue
        if dist[nx][ny] == 0 and board[nx][ny] == 0:
            # 방문한 적이 없고, 안 익은 토마토가 들어있다면
            q.append((nx,ny))
            dist[nx][ny] = dist[x][y] + 1
            max_cnt = max(max_cnt,dist[nx][ny])
            
for i in range(N):
    for j in range(M):
        if board[i][j] == 0 and dist[i][j] == 0: # 익지 않은 토마토인데 방문한 적이 없다면
            print(-1)
            exit(0)
print(max_cnt)

# answer
from collections import deque

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

Q = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            Q.append((i, j))
            dist[i][j] = 0
        if board[i][j] == 0:
            dist[i][j] = -1

while Q:
    cur = Q.popleft()
    for dir in range(4):
        nx = cur[0] + dx[dir]
        ny = cur[1] + dy[dir]
        if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1:
            dist[nx][ny] = dist[cur[0]][cur[1]] + 1
            Q.append((nx, ny))

ans = 0
for i in range(n):
    for j in range(m):
        if dist[i][j] == -1:
            print(-1)
            exit(0)
        ans = max(ans, dist[i][j])

print(ans)
