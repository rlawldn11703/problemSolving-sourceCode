def OOB(nx,ny,n):
    if nx < 0:
        nx = n + nx
    if ny < 0:
        ny = n + ny
    nx %= n
    ny %= n
    return nx,ny
    
def move(d,p,n,locs):
    dx = [0,0,-1,-1,-1,0,1,1,1]
    dy = [0,1,1,0,-1,-1,-1,0,1]
    new_loc = []
    for x,y in locs:
        nx,ny = x+p*dx[d],y+p*dy[d]
        nx,ny = OOB(nx,ny,n)
        new_loc.append((nx,ny))
    return new_loc

n,m = map(int,input().split())
board = []
for _ in range(n):
    row = list(map(int,input().split()))
    board.append(row)

nut = [(n-1,0),(n-2,0),(n-1,1),(n-2,1)]

for _ in range(m):
    # m번째 년도의 이동 규칙
    d,p = map(int,input().split())
    # 1단계 : 영양제 규칙에 따라 이동
    nut = move(d,p,n,nut)
    ck = [[False]*n for _ in range(n)]
    # 3단계 : 성장하는 리브로수 계산
    dx,dy = [-1,-1,1,1],[1,-1,-1,1]
    for x,y in nut:
        # 해당 년도에 특수 영양제 맞았는지 확인
        ck[x][y] = True
        # 특수 영양제가 있는 땅의 리브로수는 높이가 1만큼 증가
        board[x][y] += 1
    for x,y in nut:
        cnt = 0
        for w in range(4):
            nx,ny = x+dx[w],y+dy[w]
            # 대각선으로 인접한 방향이 격자를 벗어나는 경우에는 세지 않아야 함.
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 특수 영양제를 투입한 리브로수의 대각선으로 인접한 방향에 높이가 1 이상인 리브로수가 있는 만큼 높이가 더 성장
            if board[nx][ny] >= 1:
                cnt += 1
        board[x][y] += cnt
    
    # 새로 영양제 투입할 땅 결정
    nut = []
    for i in range(n): 
        for j in range(n):
            # 해당 년도에 특수 영양제를 맞은 땅 제외
            if ck[i][j]:
                continue
            if board[i][j] >= 2:
                board[i][j] -= 2
                # 해당 땅 위에 특수 영양제
                nut.append((i,j))

print(sum([sum(row) for row in board]))
