from collections import deque,defaultdict
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
def rotate(board,cnt):
    # 초기 보드 그대로 리턴
    if cnt == 0:
        return board
    new_board = [[0]*n for _ in range(n)]
    # 십자가 모양 반시계 방향 회전 
    counter_clock = list(map(list,zip(*board)))[::-1]
    for i in range(n):
        new_board[i][n//2] = counter_clock[i][n//2]
        new_board[n//2][i] = counter_clock[n//2][i]
    # 4개의 정사각형 시계 방향 회전
    size = n//2
    # 초기 사각형 시작 위치
    x_start,y_start = [0,0,size+1,size+1], [0,size+1,0,size+1]
    for x,y in zip(x_start,y_start):
        # part: 작은 사각형
        part = [[0]*size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                nx,ny = x+i,y+j
                part[i][j] = board[nx][ny]
        part = list(map(list,zip(*part[::-1])))
        for i in range(size):
            for j in range(size):
                nx,ny = x+i,y+j
                new_board[nx][ny] = part[i][j]
    return new_board

def bfs(board):
    touch = defaultdict(int) # 어떤 그룹끼리 변이 몇번 접했는지
    group_dict = {} # 그룹마다 어떤 숫자, 몇개 속해있는지 카운트
    group, ck= [[0]*n for _ in range(n)], [[False]*n for _ in range(n)]
    dx,dy = [1,0,-1,0],[0,1,0,-1]
    g = 0
    for i in range(n):
        for j in range(n):
            if not ck[i][j]:
                g += 1
                q = deque([(i,j,board[i][j])])
                group_dict[g] = [board[i][j],1]
                group[i][j] = g
                ck[i][j] = True
                while q:
                    x,y,num = q.popleft()
                    for w in range(4):
                        nx,ny = x+dx[w],y+dy[w]
                        # OOB check
                        if nx<0 or nx>=n or ny<0 or ny>=n:
                            continue
                        if board[nx][ny] == num and not ck[nx][ny]: # 같은 숫자고 방문한 적 없다면! 
                            ck[nx][ny] = True
                            group_dict[g][1] += 1
                            group[nx][ny] = g
                            q.append((nx,ny,num))
                        # 변이 맞닿아있는 그룹 계산하기
                        if board[nx][ny] != num and group[nx][ny] != 0: # 다른 숫자고 이미 그룹이 존재한다면(더 숫자 작음)
                            touch[(group[nx][ny],g)] += 1
    return touch,group_dict
def cal_artistry(touch:dict,group_dict:dict):
    art= 0
    for k,v in touch.items():
        f,s = k
        art += group_dict[f][0]*group_dict[s][0]*v*(group_dict[f][1]+group_dict[s][1])
    return art

ans = 0
for cnt in range(4):
    board = rotate(board,cnt)
    touch,group_dict = bfs(board)
    ans += cal_artistry(touch,group_dict)
print(ans)