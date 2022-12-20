from collections import deque
def solution():
    n,k = int(input()),int(input())
    Map = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for _ in range(k):
        r,c = map(int,input().split())
        Map[r][c] = 1
    L,dir = int(input()),[]
    for _ in range(L):
        x,d = input().split()
        dir.append((int(x),d))
    time,i,now = 0,0,0
    dx,dy = [0,1,0,-1],[1,0,-1,0]
    snake = deque([(1,1)])
    while True:
        time += 1
        nx,ny = snake[-1][0]+dx[now],snake[-1][1]+dy[now]
        if nx<1 or nx>n or ny<1 or ny>n:
            return time
        if (nx,ny) in snake:
            return time
        snake.append((nx,ny))
        if Map[nx][ny] == 1:
            Map[nx][ny] = 0
        else:
            snake.popleft()
        if i < len(dir) and time==dir[i][0]:
            if dir[i][1] == 'L':
                now = 3 if now==0 else now-1
            else:
                now = (now+1)%4
            i += 1
print(solution())
