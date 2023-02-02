from collections import deque
n,k = map(int,input().split())
test,virus = [],deque([])
for i in range(n):
    test.append(list(map(int,input().split())))
    for j in range(n):
        if test[i][j] > 0:
            virus.append((i,j))
rnd = [[-1]*n for _ in range(n)]
s,i,j = map(int,input().split())
dx,dy = [1,0,-1,0],[0,1,0,-1]
for r in range(s):
    v = len(virus)
    while v>0:
        x,y = virus.popleft()
        v -= 1
        for w in range(4):
            nx,ny = x+dx[w],y+dy[w]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if test[nx][ny]==0: #비어있다면
                test[nx][ny]=test[x][y] #전염시키기
                rnd[nx][ny] = r
                virus.append((nx,ny))
            elif rnd[nx][ny]==r: #바이러스가 존재하면서 해당 초에 감염된 것이라면
                test[nx][ny] = min(test[nx][ny],test[x][y])
                virus.append((nx,ny))
print(test[i-1][j-1])
