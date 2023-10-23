from collections import deque
def bfs(maps,ck,start):
    dx,dy = [1,0,-1,0],[0,1,0,-1]
    days = int(maps[start[0]][start[1]])
    n,m = len(maps),len(maps[0])
    q = deque([start])
    while q:
        x,y = q.popleft()
        for w in range(4):
            nx,ny = x+dx[w],y+dy[w]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if not ck[nx][ny] and maps[nx][ny] != 'X':
                ck[nx][ny] = True
                days += int(maps[nx][ny])
                q.append((nx,ny))
    return days
def solution(maps):
    n,m = len(maps),len(maps[0])
    answer = []
    ck = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not ck[i][j] and maps[i][j] != 'X':
                ck[i][j] = True
                day = bfs(maps,ck,(i,j))
                answer.append(day)
    answer.sort()
    if not answer:
        answer.append(-1)
    return answer