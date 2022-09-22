from collections import deque
n,m = map(int,input().split())
board = []
for _ in range(n):
    board.append(input())
visited = [[False for _ in range(m)] for _ in range(n)]
dx,dy = [1,0,-1,0],[0,1,0,-1]
count = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == '0' and not visited[i][j]:
            q = deque([(i,j)])
            count += 1
            while q:
                x,y = q.popleft()
                for w in range(4):
                    nx,ny = x+dx[w],y+dy[w]
                    if nx<0 or nx>=n or ny<0 or ny>=m:
                        continue
                    if board[nx][ny]=='0' and not visited[nx][ny]:
                        q.append((nx,ny))
                        visited[nx][ny] = True
print(count)
