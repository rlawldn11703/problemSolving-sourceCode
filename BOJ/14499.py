n,m,x,y,k = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
def OOB(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return True
    return False
def roll_dice(dice,cmd):
    new_dice = dice[:]
    '''
    윗면이 1이고, 동쪽을 바라보는 방향이 3
        [2]
     [4][1][3]
        [5]
        [6]
    '''
    change_map = [{},{1:4,3:1,4:6,6:3},{1:3,3:6,4:1,6:4},{2:1,1:5,5:6,6:2},{2:6,1:2,5:1,6:5}]
    change = change_map[cmd]
    for ex,new in change.items():
        new_dice[ex] = dice[new]
    return new_dice

def roll_dice_new(dice,cmd):
    '''
    윗면이 2이고, 동쪽을 바라보는 방향이 6
       [1]
    [5][2][6]
       [3]
       [4]
    '''
    idx = [
        [],
        [2, 6, 4, 5],  # 동쪽, 5->2, 2->6, 6->4, 4->5
        [2, 5, 4, 6], # 서쪽, 6->2, 2->5, 5->4, 4->6
        [3, 2, 1, 4], # 북쪽, 4->3, 3->2, 2->1, 1->4
        [2, 3, 4, 1] # 남쪽, 1->2, 2->3, 3->4, 4->1
    ]
    tmp = dice[:]
    for i in range(4):
        tmp[idx[cmd][i]] = dice[idx[cmd][(i + 1) % 4]]
    return tmp

cmd_list = list(map(int,input().split()))
# [0,동,서,북,남]
dx,dy = [0,0,0,-1,1],[0,1,-1,0,0]
dice = [0] * 7
for cmd in cmd_list:
    nx,ny = x+dx[cmd],y+dy[cmd]
    if OOB(nx,ny):
        continue
    x,y = nx,ny
    dice = roll_dice(dice,cmd)
    if board[x][y] == 0:
        board[x][y] = dice[-1]
    else:
        dice[-1] = board[x][y] 
        board[x][y] = 0
    print(dice[1])
