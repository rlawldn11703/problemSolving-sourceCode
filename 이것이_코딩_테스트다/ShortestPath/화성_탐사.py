# My Code
from collections import deque
T = int(input())
for _ in range(T):
    n = int(input())
    cost,s_cost = [],[[int(1e9)]*n for _ in range(n)]
    for _ in range(n):
        cost.append(list(map(int,input().split())))
    q = deque([(0,0)])
    dx,dy = [-1,0,1,0],[0,1,0,-1]
    s_cost[0][0] = cost[0][0]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                new_cost = s_cost[x][y]+cost[nx][ny]
                if s_cost[nx][ny] > new_cost:
                    s_cost[nx][ny] = new_cost
                    q.append((nx,ny))
    print(s_cost[n-1][n-1])
# Solution(using dijkstra)
import heapq
T = int(input())
for _ in range(T):
    n = int(input())
    Board,s_cost = [],[[int(1e9)]*n for _ in range(n)]
    for _ in range(n):
        Board.append(list(map(int,input().split())))
    q = []
    heapq.heappush(q,(Board[0][0],0,0))
    s_cost[0][0] = Board[0][0]
    dx,dy = [-1,0,1,0],[0,1,0,-1]
    while q:
        cost,x,y = heapq.heappop(q)
        if s_cost[x][y] < cost:
            continue
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                new_cost = cost+Board[nx][ny]
                if s_cost[nx][ny] > new_cost:
                    s_cost[nx][ny] = new_cost
                    heapq.heappush(q,(new_cost,nx,ny))
    print(s_cost[n-1][n-1])
