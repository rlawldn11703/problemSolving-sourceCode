n,m = map(int,input().split())
data,temp = [],[[0]*m for _ in range(n)]
for _ in range(n):
    data.append((list(map(int,input().split()))))
result = 0
def virus(x,y): #dfs이용해 각 바이러스가 사방으로 퍼지도록 하기
    dx,dy = [1,0,-1,0],[0,1,0,-1]
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if temp[nx][ny]==0:
                temp[nx][ny]=2
                virus(nx,ny)
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                score += 1
    return score
def dfs(count):
    global result
    if count==3: #울타리가 3개 설치된 경우
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)
        result = max(result,get_score())
        return
    for i in range(n): #빈 공간에 울타리 설치
        for j in range(m):
            if data[i][j]==0:
                data[i][j]=1
                count += 1
                dfs(count)
                data[i][j]=0
                count -= 1
dfs(0)
print(result)
#나동빈 강사님 답안
#python3로 제출시,시간초과
