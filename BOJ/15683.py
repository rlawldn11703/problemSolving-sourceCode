from collections import deque
from copy import deepcopy
N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
# brute-force
ans  = int(1e9)
cctv = []
for i in range(N):
    for j in range(M):
        if board[i][j] >= 1 and board[i][j] <= 5:
            cctv.append((i,j,board[i][j]))
dx,dy = [-1,0,1,0],[0,1,0,-1]
def find_blind_spot(board):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                cnt += 1
    return cnt
def check_board(board,dir,num,i):
    '''
    1 -> [dir]
    2 -> [dir,dir+2]
    3 -> [dir,(dir+1)%4]
    4 -> [dir,(dir+1)%4,(dir+2)%4]
    5 -> [0,1,2,3]
    '''
    w_arr = [[dir],[dir,dir+2],[dir,(dir+1)%4],[dir,(dir+1)%4,(dir+2)%4],[0,1,2,3]]
    way = w_arr[num-1]
    board_copy = deepcopy(board)
    for w in way: 
        q = deque([(cctv[i][0],cctv[i][1])])
        while q:
            x,y = q.popleft()
            nx,ny = x+dx[w],y+dy[w]
            if 0<=nx<N and 0<=ny<M:
                if board_copy[nx][ny] != 6:
                    board_copy[nx][ny] = '#'
                    q.append((nx,ny))
    return board_copy
# 한 방향에 대해 depth 끝까지 넣는 형태로 구현하기
def dfs(board,i):
    global ans
    if i >= len(cctv):
        ans = min(ans,find_blind_spot(board))
        return 
    dir_list = [4,2,4,4,1]
    cctv_num = cctv[i][-1]
    for dir in range(dir_list[cctv_num-1]): # 회전
        board_copy = check_board(board,dir,cctv_num,i)
        dfs(board_copy,i+1)
dfs(board,0) 
print(ans)

# answer
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]  # 남쪽, 동쪽, 북쪽, 서쪽 순서
n, m = map(int, input().split())
board1 = [list(map(int, input().split())) for _ in range(n)]
# 최초에 입력받은 board를 저장할 변수
board2 = [[0] * m for _ in range(n)]
# 사각 지대의 개수를 세기 위해 사용할 변수
cctv = []
# cctv의 좌표를 저장할 변수

def OOB(a, b):  # Out Of Bounds 확인
    return a < 0 or a >= n or b < 0 or b >= m

def upd(x, y, dir):
    '''
    (x,y)에서 dir 방향으로 진행하면서 벽을 만날 때 까지 지나치는 모든 빈칸을 7로 바꿔버림
    '''
    dir %= 4
    while True:
        x += dx[dir]
        y += dy[dir]
        if OOB(x, y) or board2[x][y] == 6: # 범위를 벗어났거나 벽을 만나면 함수를 탈출
            return
        if board2[x][y] != 0: # 해당 칸이 빈칸이 아닐 경우(=cctv가 있을 경우) 넘어감
            continue
        board2[x][y] = 7

mn = 0  # 사각 지대의 최소 크기 (=답)
for i in range(n): 
    for j in range(m):
        if board1[i][j] != 0 and board1[i][j] != 6:
            cctv.append((i, j))
        if board1[i][j] == 0:
            mn += 1

for tmp in range(1 << (2 * len(cctv))):
    # tmp를 4진법으로 뒀을 때 각 자리수를 cctv의 방향으로 생각할 것이다.
    for i in range(n): # deepcopy
        for j in range(m):
            board2[i][j] = board1[i][j]
    brute = tmp
    for i in range(len(cctv)):
        dir = brute % 4
        brute //= 4
        x, y = cctv[i]
        if board1[x][y] == 1:
            upd(x, y, dir)
        elif board1[x][y] == 2:
            upd(x, y, dir)
            upd(x, y, dir + 2)
        elif board1[x][y] == 3:
            upd(x, y, dir)
            upd(x, y, dir + 1)
        elif board1[x][y] == 4:
            upd(x, y, dir)
            upd(x, y, dir + 1)
            upd(x, y, dir + 2)
        else:  # board1[x][y] == 5
            upd(x, y, dir)
            upd(x, y, dir + 1)
            upd(x, y, dir + 2)
            upd(x, y, dir + 3)
    val = sum(row.count(0) for row in board2)
    mn = min(mn, val)

print(mn)
