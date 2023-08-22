from collections import deque
N = int(input())
board = [list(input()) for _ in range(N)]
ans1,ans2 = 0,0
ck1,ck2 = [[False]*N for _ in range(N)],[[False]*N for _ in range(N)]
dx,dy = [1,0,-1,0],[0,1,0,-1]
for i in range(N):
    for j in range(N):
        c = board[i][j]
        if not ck1[i][j]: # 적록 색약인 사람
            q1 = deque([(i,j)])
            ans1 += 1
            while q1:
                x,y = q1.popleft()
                for dir in range(4):
                    nx,ny = x+dx[dir],y+dy[dir]
                    if nx < 0 or nx >= N or ny <0 or ny>=N:
                        continue
                    if c == 'B':
                        if not ck1[nx][ny] and board[nx][ny] == c:
                            ck1[nx][ny] = True
                            q1.append((nx,ny))
                    else:
                        if not ck1[nx][ny] and board[nx][ny] != 'B':
                            ck1[nx][ny] = True
                            q1.append((nx,ny))
        if not ck2[i][j]: # 적록 색약이 아닌 사람
            q2 = deque([(i,j)])
            ans2 += 1
            while q2:
                x,y = q2.popleft()
                for dir in range(4):
                    nx,ny = x+dx[dir],y+dy[dir]
                    if nx < 0 or nx >= N or ny <0 or ny>=N:
                        continue
                    if not ck2[nx][ny] and board[nx][ny] == c:
                        ck2[nx][ny] = True
                        q2.append((nx,ny))
print(ans2,ans1)

# answer
n = int(input())
board = [list(input()) for _ in range(n)]
vis = [[False] * n for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(i, j):
    Q = deque([(i, j)])
    vis[i][j] = True
    while Q:
        cur = Q.popleft()
        for dir in range(4):
            nx = cur[0] + dx[dir]
            ny = cur[1] + dy[dir]
            if 0 <= nx < n and 0 <= ny < n:
                if not vis[nx][ny] and board[i][j] == board[nx][ny]:
                    vis[nx][ny] = True
                    Q.append((nx, ny))

def area():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not vis[i][j]:
                cnt += 1
                bfs(i, j)
    return cnt

not_g = area()  # 적록색약이 아닌 사람

# 적록색약인 사람을 구하기 위한 방문 배열 초기화
vis = [[False] * n for _ in range(n)]

# 적록색약은 초록과 빨강을 구분 못하므로 초록이면 빨강으로 바꿔줌
for i in range(n):
    for j in range(n):
        if board[i][j] == 'G':
            board[i][j] = 'R'

is_g = area()  # 적록색약인 사람
print(not_g, is_g)
