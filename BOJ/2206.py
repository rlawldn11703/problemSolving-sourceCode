from collections import deque
N,M = map(int,input().split())
board = [list(map(int,list(input()))) for _ in range(N)]
dx,dy = [1,0,-1,0],[0,1,0,-1]
dist = [[[0,0] for _ in range(M)] for _ in range(N)]
# 0은 벽을 부수지 않고 이동했을경우, 1은 벽을 하나만 부수고 이동했을 경우
dist[0][0][0],dist[0][0][1] = 1,1
def bfs():
    q = deque([(0,0,0)])
    while q:
        x,y,ck = q.popleft()
        # ck : false면 0, True면 1
        if x == N-1 and y == M-1:
            return dist[N-1][M-1][ck]
        for w in range(4):
            nx,ny = x+dx[w],y+dy[w]
            if nx < 0 or nx >= N or ny < 0 or ny >= M :
                continue
            # 이동할 수 있는 곳으로
            if board[nx][ny] == 0 and dist[nx][ny][ck] == 0:
                dist[nx][ny][ck] = dist[x][y][ck]+ 1
                q.append((nx,ny,ck))
            # (nx, ny)를 부수는 경우
            if not ck and board[nx][ny] == 1 and dist[nx][ny][1] == 0:
                dist[nx][ny][1] = dist[x][y][0] + 1
                q.append((nx,ny,1))
    return -1
# 한번도 도착한 적이 없으면(불가능하면)
print(bfs())
