from collections import deque
n,m = map(int,input().split())
board = []
for _ in range(n):
    board.append(input())
c_map = [[0 for _ in range(m)] for _ in range(n)]
c_map[0][0] = int(board[0][0])
dx,dy = [1,0,-1,0],[0,1,0,-1]
q = deque([(0,0)])
while q:
    x,y = q.popleft()
    for w in range(4):
        nx,ny = x+dx[w],y+dy[w]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if board[nx][ny]=='1' and c_map[nx][ny]==0 :
            c_map[nx][ny] = c_map[x][y]+1
            q.append((nx,ny))
[print(i) for i in c_map]
print(c_map[n-1][m-1])
