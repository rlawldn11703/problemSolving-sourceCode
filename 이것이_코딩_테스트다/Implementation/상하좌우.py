n = int(input())
arr = list(input().split())
x,y = 1,1
move = {'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}
for dir in arr:
    nx,ny = x+move[dir][0],y+move[dir][1]
    if nx < 1 or nx > n or ny<1 or ny > n:
        continue
    x,y = nx,ny
print(x,y)
