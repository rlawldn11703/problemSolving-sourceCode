from collections import deque
R,C = map(int,input().split())
board = [list(input()) for _ in range(R)]
dist = [[int(1e9)]*C for _ in range(R)]
dx,dy = [1,0,-1,0] , [0,1,0,-1]
fire,jh = deque([]), deque([])
for i in range(R):
    for j in range(C):
        if board[i][j] == 'J':
            jh.append((i,j,0))
            dist[i][j] = 0
        elif board[i][j] == 'F':
            fire.append((i,j,0))
minute,ck = 0,True
while ck:
    minute += 1 
    while fire and fire[0][-1] < minute: # 불의 이동
        x,y,t = fire.popleft()
        for w in range(4):
            nx,ny = x+dx[w],y+dy[w]
            if nx < 0 or nx >= R or ny <0 or ny >= C:
                continue
            if board[nx][ny] == '.':
                board[nx][ny] = 'F'
                fire.append((nx,ny,minute))
    while jh and jh[0][-1] < minute: # 지훈이 이동
        x,y,t= jh.popleft()
        for w in range(4):
            nx,ny = x+dx[w],y+dy[w]
            if nx < 0 or nx >= R or ny <0 or ny >= C: # 탈출 성공
                print(minute)
                exit(0)
            if board[nx][ny] == '.' and dist[nx][ny]> minute:
                dist[nx][ny] = minute
                jh.append((nx,ny,minute))   
    if not fire and not jh:
        ck = False
print('IMPOSSIBLE')

# answer
from collections import deque

n, m = map(int, input().split())
board = [input() for _ in range(n)]
dist1 = [[-1] * m for _ in range(n)]  # 불의 전파 시간
dist2 = [[-1] * m for _ in range(n)]  # 지훈이의 이동 시간
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

Q1 = deque()
Q2 = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 'F':
            Q1.append((i, j))
            dist1[i][j] = 0
        if board[i][j] == 'J':
            Q2.append((i, j))
            dist2[i][j] = 0

# 불에 대한 BFS
while Q1:
    cur = Q1.popleft()
    for dir in range(4):
        nx = cur[0] + dx[dir]
        ny = cur[1] + dy[dir]
        if 0 <= nx < n and 0 <= ny < m and dist1[nx][ny] == -1 and board[nx][ny] != '#':
            dist1[nx][ny] = dist1[cur[0]][cur[1]] + 1
            Q1.append((nx, ny))

# 지훈이에 대한 BFS
while Q2:
    cur = Q2.popleft()
    for dir in range(4):
        nx = cur[0] + dx[dir]
        ny = cur[1] + dy[dir]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            print(dist2[cur[0]][cur[1]] + 1)
            exit(0)
        if 0 <= nx < n and 0 <= ny < m and dist2[nx][ny] == -1 and board[nx][ny] != '#':
            if dist1[nx][ny] == -1 or dist1[nx][ny] > dist2[cur[0]][cur[1]] + 1:
                dist2[nx][ny] = dist2[cur[0]][cur[1]] + 1
                Q2.append((nx, ny))

print("IMPOSSIBLE")
