n,m = map(int,input().split())
x,y,d = map(int,input().split())
M,visited = [['1']*(m+2)],[[False for _ in range(m+2)] for _ in range(n+2)]
for _ in range(n):
    M.append(['1']+input().split()+['1'])
M.append(['1']*(m+2))
dx,dy = [-1,0,1,0],[0,1,0,-1]
x,y = x+1,y+1
ans,visited[x][y] = 1,True
while True:
    ck,dir = False,d
    for _ in range(4):
        nx,ny = x+dx[dir-1],y+dy[dir-1]
        dir = dir-1 if dir>0 else 3
        if M[nx][ny]=='0' and not visited[nx][ny]:
            visited[nx][ny] = True
            x,y = nx,ny
            ans += 1
            ck,d = True,dir
            break
    if not ck:
        nx,ny = x-dx[d],y-dy[d]
        if M[nx][ny]=='1':
            break
        x,y = nx,ny 
print(ans)
