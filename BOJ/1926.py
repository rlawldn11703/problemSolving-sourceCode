from collections import deque
n,m = map(int,input().split())
paper = []
ck = [[False]*m for _ in range(n)]
cnt,max_area = 0,-1
dx,dy = [1,0,-1,0],[0,1,0,-1]
for _ in range(n):
    paper.append(input().split())
for i in range(n):
    for j in range(m):
        area = 0
        if paper[i][j] == '1' and not ck[i][j]:
            q = deque([(i,j)])
            ck[i][j] = True
            area +=  1
            cnt += 1
            while q:
                x,y = q.popleft()
                for w in range(4):
                    nx,ny = x+dx[w],y+dy[w]
                    if nx < 0  or nx >= n or ny < 0 or ny >= m:
                        continue
                    if paper[nx][ny] == '1' and not ck[nx][ny]:
                        q.append((nx,ny))
                        ck[nx][ny] = True
                        area += 1
        max_area = max(max_area,area)
print(cnt)
print(max_area)
