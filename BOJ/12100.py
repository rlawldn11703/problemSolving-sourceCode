n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
ans = 0
# 한 번의 이동 (상,하,좌,우)
def rotate_and_merge(board,dir):
    '''
    zip(*iterable)
    zip 함수는 여러 개의 iterable한 객체를 인자로 받아, 각 객체에서 동일한 인덱스 위치에 있는 요소들을 튜플로 묶어줌.
    이때, * 연산자는 인자를 언패킹하여 zip 함수에 전달하는 역할
    '''
    for _ in range(dir):
        board = list(map(list,zip(*board[::-1])))
    new_board = []
    for i in range(n):
        nonzero = []
        for j in range(n):
            if board[i][j] != 0:
                nonzero.append(board[i][j])
        merged = []
        idx = len(nonzero)-1
        while idx >= 0:
            if idx >= 1 and nonzero[idx] == nonzero[idx-1] :
                merged.append(nonzero[idx] * 2) # 합쳐져서 값이 두배
                idx -= 2
            else:
                merged.append(nonzero[idx])
                idx -= 1
        n_zero = n-len(merged)
        new_row = [0]* n_zero + merged[::-1]
        new_board.append(new_row)
    return new_board
def dfs(board,cnt):
    global ans
    if cnt == 6:
        return
    ans = max(ans,max([max(row) for row in board]))
    for dir in range(4):
        # 회전을 통해 4 방향으로 미는 것 구현 가능
        dfs(rotate_and_merge(board,dir),cnt+1)
dfs(board,0)
print(ans)
