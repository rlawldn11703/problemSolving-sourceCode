from collections import deque
n,m,q = map(int,input().split())
board = [[0 for _ in range(m)] for _ in range(n)]
def tilt(board,num):
    nb = []
    for j in range(m): # 한 열에 대해서
        nonzero = []
        for i in range(n):
            if board[i][j] != 0:
                nonzero.append(board[i][j])
        if num == 2: # 위로 기울이기 때문에 0이 바닥으로
            nb.append(nonzero+[0]* (n-len(nonzero)))
        else:
            nb.append([0]* (n-len(nonzero))+nonzero)
    return list(map(list,zip(*nb)))
def remove(board):
    dx,dy = [1,0,-1,0],[0,1,0,-1]
    visited = [[False] * m for _ in range(n)]
    ck = False # 제거 대상이 있는지 확인
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 :
                num = board[i][j]
                q = deque([(i,j)])
                visited[i][j] = True
                delete = [(i,j)]
                while q:
                    x,y = q.popleft()
                    for w in range(4):
                        nx,ny = x+dx[w],y+dy[w]
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            continue
                        if board[nx][ny] == num and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx,ny))
                            delete.append((nx,ny))
                if len(delete) > 1 :
                    ck = True 
                    for x,y in delete:
                        board[x][y] = 0
    return board,ck


for _ in range(q):
    cmd = input().split()
    if cmd[0] == '1':
        c,x,y,v = map(int,cmd)
        board[x-1][y-1] = max(board[x-1][y-1],int(v))
    elif cmd[0] == '2' or cmd[0] == '3' :
        while True:
            board = tilt(board,int(cmd[0])) # 보드 기울이기
            board,ck = remove(board)
            if not ck:
                break
    else:
        c,x,y = map(int,cmd)
        board[x-1][y-1] = 0
for i in range(n):
    print(*board[i])