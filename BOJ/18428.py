from itertools import combinations
from collections import deque
def check(M,n,teacher):
    dx,dy = [1,0,-1,0],[0,1,0,-1]
    for x,y in teacher:
        dir = [True]*4
        for w in range(1,n+1):
            for i in range(4):
                if dir[i]:
                    xx,yy = x+w*dx[i],y+w*dy[i]
                    if xx<0 or xx>=n or yy<0 or yy>=n:
                        dir[i] = False
                        continue
                    if M[xx][yy]=='S':
                        return False
                    if M[xx][yy]=='O':
                        dir[i] = False
    return True
n = int(input())
hall,empty,T,ck = [],[],[],False #empty:빈칸,T:선생님
for _ in range(n):
    hall.append(input().split())
for i in range(n):
    for j in range(n):
        if hall[i][j] == 'T':
            T.append((i,j))
        elif hall[i][j]=='X':
            empty.append((i,j))
for obs in combinations(empty,3):
    for x,y in obs:
        hall[x][y]='O'
    if check(hall,n,T):
        ck = True
        break
    else:
        for x,y in obs:
            hall[x][y] = 'X'
if ck:
    print('YES')
else:
    print('NO')
