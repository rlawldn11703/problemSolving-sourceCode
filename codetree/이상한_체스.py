# 헷갈리지 말 것!
# 한 번 이동해서 4 방향으로 갈 수 있는 것과 한 방향으로 쭉 멀리 갈 수 있는 것 다르니까 생각하고 짜기
from copy import deepcopy
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
def OOB(x,y):
    return x<0 or x>=n or y<0 or y>=m
def rotate(piece,d):
    dx_list = [[],[-1],[0,0],[-1,0],[0,-1,0],[-1,0,1,0]]
    dy_list = [[],[0],[-1,1],[0,1],[-1,0,1],[0,1,0,-1]]
    dxs,dys = dx_list[piece],dy_list[piece]
    if d == 0:
        return dxs,dys
    elif d == 1:
        dxs = [-dx for dx in dxs]
        return dxs,dys
    elif d == 2:
        return dys,dxs
    else:
        dxs = [-dx for dx in dxs]
        return dys,dxs

def cnt_not_available(ck):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if ck[i][j] == 0:
                cnt += 1
    return cnt

# 우리편 말의 위치와 어떤 말인지 저장    
mine = []
for i in range(n):
    for j in range(m):
        if board[i][j] >=1 and board[i][j] <= 5:
            mine.append((i,j,board[i][j]))
k = len(mine) # 내 편 말의 개수
ans = 100
for tmp in range(4**k):
    brute = tmp
    ds = []
    for _ in range(k):
        d = brute % 4
        brute //= 4
        ds.append(d) # 회전 방향
    ck = deepcopy(board)
    for idx in range(k):
        x,y,piece = mine[idx]
        direction  = ds[idx]
        dx,dy = rotate(piece,direction)
        for w in range(len(dx)):
            nx,ny = x,y
            while True:
                nx += dx[w]
                ny += dy[w]
                if OOB(nx,ny) or board[nx][ny] == 6: # 범위 밖으로 나가거나 상대편 말을 만난 경우
                    break
                ck[nx][ny] = piece
    cnt = cnt_not_available(ck)
    ans = min(ans,cnt)
print(ans)
            
# 방향 결정 풀이 다른 방식으로! 
def fill(start_x, start_y, piece_num, face_dir,ck):
    # 북동남서 순으로 방향을 설정합니다.
    can_move = [
    [],
    [1, 0, 0, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
    ]
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    for i in range(4):
        # 해당 말이 움직일 수 있는 방향인지를 확인합니다.
        # 움직일 수 없다면 pass합니다.
        if not can_move[piece_num][i]:
            continue
        # 갈 수 있다면, 끝날때까지 계속 진행합니다.
        # 방향은 face_dir만큼 시계방향으로 
        # 회전했을 때를 기준으로 움직입니다.
        x, y = start_x, start_y
        move_dir = (i + face_dir) % 4
        while True:
            ck[x][y] = piece
            nx, ny = x + dxs[move_dir], y + dys[move_dir]
            if not OOB(nx, ny) and board[nx][ny] != 6:
                x, y = nx, ny
            else:
                break
    return ck
for tmp in range(4**k):
    brute = tmp
    ds = []
    for _ in range(k):
        d = brute % 4
        brute //= 4
        ds.append(d) # 회전 방향
    ck = deepcopy(board)
    for idx in range(k):
        x,y,piece = mine[idx]
        direction  = ds[idx]
        ck = fill(x,y,piece,direction,ck)
    cnt = cnt_not_available(ck)
    ans = min(ans,cnt)
print(ans)


