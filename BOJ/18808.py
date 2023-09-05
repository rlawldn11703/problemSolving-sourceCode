N,M,K = map(int,input().split())
board = [[0]* M for _ in range(N)]
# i번째 스티커에 대해 90,180,270 회전 -> 함수로 
# 4* 100* 40 * 40
def attach(board,sticker):
    '''
    노트북에 스티커를 붙일 수 있는지 확인하는 함수
    '''
    R,C = len(sticker),len(sticker[0])
    for i in range(N-R+1):
        for j in range(M-C+1):
            if can_attach(board,sticker,i,j):
                # sticker 붙일 수 있다면 붙이기
                for r in range(R):
                    for c in range(C):
                        if sticker[r][c] == 1:
                            board[i+r][j+c] = sticker[r][c]
                return False
    return True
                        
def can_attach(board,sticker,i,j):
    R,C = len(sticker),len(sticker[0])
    for x in range(R):
        for y in range(C):
            if sticker[x][y] == 1 and board[i+x][j+y] == 1:
                return False
    return True

for _ in range(K):
    R,C = map(int,input().split())
    sticker = [list(map(int,input().split()))for _ in range(R)]
    cnt,ck = 0,True
    while ck and cnt <= 3:
        # 붙일 수 있는 지 확인하기
        ck = attach(board,sticker)
        cnt += 1
        # 시계 방향으로 90도 회전
        sticker = list(map(list,zip(*sticker[::-1])))
ans = sum([sum(board[i]) for i in range(N)])
print(ans)
