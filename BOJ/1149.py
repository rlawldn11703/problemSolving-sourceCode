from collections import deque
N = int(input())
cost = [list(map(int,input().split())) for _ in range(N)]
min_cost = [[int(1e9)]*3 for _ in range(N)]
min_cost[0] = cost[0]
q = deque([(0,0),(0,1),(0,2)])
while q:
    x,y = q.popleft()
    if x==N-1:
        continue
    for yy in range(3):
        if yy != y:
            dist = min_cost[x][y] + cost[x+1][yy]
            if dist < min_cost[x+1][yy]:
                min_cost[x+1][yy] = dist
                q.append((x+1,yy))
print(min(min_cost[-1]))
