move = [(-1,0,0),(1,0,0),(0,-1,1),(0,1,1)]
col = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
now,ans = input(),0
x,y = int(now[1]),col[now[0]]
for dx,dy,d1 in move:
    nx,ny = x+dx*2,y+dy*2
    for xx,yy,d2 in move:
        if d1 != d2:
            nx,ny = nx+xx,ny+yy
            if 1<=nx<=8 and 1<=ny<=8:
                ans += 1
print(ans)

#revised
data = input()
row,col = int(data[1]),int(ord(data[0]))-int(ord('a'))+1
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
result = 0
for step in steps:
    n_row = row+step[0]
    n_col = col+step[1]
    if n_row >=1 and n_row <= 8 and n_col >= 1 and n_col <=8:
        result += 1
print(result)
