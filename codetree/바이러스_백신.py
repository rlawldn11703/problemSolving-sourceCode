from itertools import combinations
from collections import deque

def check_virus(board,ck,n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0 and ck[i][j] == -1:
                return False
    return True

n,m = map(int,input().split())
board = []
for _ in range(n):
    row = list(map(int,input().split()))
    board.append(row)

# 병원 위치
hospitals = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            hospitals.append((i,j))

dx,dy = [1,0,-1,0],[0,1,0,-1]
max_num  = int(1e9)
ans = max_num
for hospital in combinations(hospitals,m):
    q = deque(hospital)
    ck = [[-1]*n for _ in range(n)]
    for i,j in hospital:
        ck[i][j] = 0
    # bfs
    while q:
        x,y = q.popleft()
        for w in range(4):
            nx,ny = x+dx[w],y+dy[w]
            # OOB check
            if 0>nx or nx>=n or 0>ny or ny >= n:
                continue
            if board[nx][ny] != 1 and ck[nx][ny] == -1:
                ck[nx][ny] = ck[x][y] + 1
                q.append((nx,ny))

    # 바이러스 없애는데 걸리는 시간 -> 바이러스가 처음부터 없다면 0초 소요되니까 default = 0
    time = 0
    # 바이러스가 모두 없어졌다면
    if check_virus(board,ck,n):
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    time = max(time,ck[i][j])
        ans = min(ans,time)
if ans == max_num: # 모든 바이러스를 없앨 수 있는 방법이 없는 경우 
    print(-1)
else:
    print(ans)

