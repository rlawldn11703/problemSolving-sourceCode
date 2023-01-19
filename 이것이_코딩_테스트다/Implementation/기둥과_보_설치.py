def ck(x,y,opt,frame,n):
    col,beam = frame[0],frame[1]
    if opt==0:
        if x==0 or (0<=x-1 and col[x-1][y]==1):
            return True
        elif beam[x][y]==1 or (0<=y-1 and beam[x][y-1]==1):
            return True
        else:
            return False
    else:
        if (0<=x-1 and col[x-1][y]==1) or (0<=x-1 and y+1<=n and col[x-1][y+1]==1):
            return True
        elif (0<=y-1 and beam[x][y-1]==1) and (y+1<n and beam[x][y+1]==1):
            return True
        else:
            return False
def solution(n, build_frame):
    frame = [[[0]*(n+1) for _ in range(n+1)],[[0]*(n+1) for _ in range(n+1)]]
    for cmd in build_frame:
        c,r,a,b = cmd #x가 row,y가 col
        if b==1:
            if ck(r,c,a,frame,n):
                frame[a][r][c] = 1
        else:
            st,frame[a][r][c] = True,0
            for i in range(n+1):
                for j in range(n+1):
                    for k in range(2):
                        if frame[k][i][j]==1 and not ck(i,j,k,frame,n):
                            st = False
            if not st: # 삭제불가
                frame[a][r][c] = 1
    ans = []
    for i in range(n+1):
        for j in range(n+1):
            for k in range(2):
                if frame[k][i][j]==1: ans.append([j,i,k])
    return sorted(ans)
